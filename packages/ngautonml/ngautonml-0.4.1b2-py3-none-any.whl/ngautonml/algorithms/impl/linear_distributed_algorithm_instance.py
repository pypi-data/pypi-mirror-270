'''Base class for distributed linear algorithms.'''

# Copyright (c) 2024 Carnegie Mellon University
# This code is subject to the license terms contained in the LICENSE file.

import abc
from typing import Any, Callable, Optional, Tuple, TypeVar, Union

import numpy as np
import pandas as pd
from scipy.optimize import minimize  # type: ignore[import]

from ...algorithms.impl.algorithm import Algorithm, HyperparamError
from ...config_components.distributed_config import DistributedConfig
from ...wrangler.dataset import Dataset, DatasetKeys, RoleName
from ...wrangler.logger import Logger

from .distributed_algorithm_instance import (
    DistributedAlgorithmInstance, NeighborState, NoDataError)


logger = Logger(__file__).logger()


# These functions assume x is 1 or 2 dimensional and v is 1-dimensional


def grad_norm2(a: np.ndarray) -> np.ndarray:
    '''Return the gradient of the squared norm of a.'''
    return 2.0 * a


def grad_inner_product(a: np.ndarray, b: np.ndarray) -> np.ndarray:  # pylint: disable=unused-argument
    '''Return the gradient of the inner product of a and b.'''
    return a


def inner_product(a: np.ndarray, b: np.ndarray) -> Union[np.float64, np.ndarray]:
    '''Return the inner product of a and b.'''
    return a @ b


def norm2(a: np.ndarray) -> np.float64:
    '''Return the squared norm of a.'''
    return np.square(a).sum()  # np.linalg.norm(a) ** 2


NeighborStateSubclass = TypeVar('NeighborStateSubclass', bound='NeighborState')


class LinearNeighborState(NeighborState[NeighborStateSubclass]):
    '''Base class for Linear Neighbor States.'''
    _v: np.ndarray

    def __init__(self, v: np.ndarray) -> None:
        self._v = v

    @property
    def v(self) -> np.ndarray:
        '''The internal state of the model.'''
        return self._v

    @v.setter
    def v(self, value: np.ndarray) -> None:
        '''The internal state of the model.'''
        self._v = value

    def should_send(self,
                    distributed: DistributedConfig,
                    last_state_sent: Optional[Any]) -> bool:
        '''Determine whether to send an update to the neighbors.'''
        if last_state_sent is None:
            return True
        assert isinstance(last_state_sent, type(self))
        # check whether the model changed much. If it didn't, don't send an update
        a: np.float64 = norm2(last_state_sent.v)
        b: np.float64 = norm2(self.v)
        ab = inner_product(self.v, last_state_sent.v)
        assert isinstance(ab, np.float64)
        dist: np.float64 = a + b - 2 * ab
        return bool(dist > distributed.fit_eps)


class LinearDistributedAlgorithmInstance(DistributedAlgorithmInstance, metaclass=abc.ABCMeta):
    '''Base class for distributed linear algorithms.'''

    _lambda: np.float64
    _l2: np.float64
    _omega: np.float64

    def __init__(self,
                 parent: Algorithm,
                 distributed: DistributedConfig,
                 **kwargs):
        hyperparams = parent.hyperparams(**kwargs)
        _lambda = np.float64(hyperparams.pop('Lambda'))
        _l2 = np.float64(hyperparams.pop('L2'))
        _omega = np.float64(hyperparams.pop('omega'))
        if not isinstance(distributed, DistributedConfig):
            raise HyperparamError(
                'distributed must be a DistributedConfig, instead found '
                f'{distributed} of type {type(distributed)}')
        self._lambda = _lambda
        self._l2 = _l2
        self._omega = _omega
        self._last_dataset = None
        super().__init__(parent, distributed=distributed, **hyperparams)

    @property
    @abc.abstractmethod
    def _yhat_is_proba(self) -> bool:
        '''Is yhat probabilites?'''

    def _sort_columns(self, dataset: Dataset) -> Dataset:
        '''Sort the columns of a dataset.

        This is needed so that the linear algorithms operate
        on the same columns in the same order.
        '''
        # TODO(Piggy/Dan): If this becomes a performance problem
        retval = dataset.output()
        retval.update(dataset)
        if DatasetKeys.DATAFRAME.value in dataset:
            retval[DatasetKeys.DATAFRAME.value] = (
                dataset[DatasetKeys.DATAFRAME.value].sort_index(axis=1))
        if DatasetKeys.COVARIATES.value in dataset:
            retval[DatasetKeys.COVARIATES.value] = (
                dataset[DatasetKeys.COVARIATES.value].sort_index(axis=1))
        return retval

    @abc.abstractmethod
    def _prepare_data(self, dataset: Optional[Dataset]) -> Tuple[np.ndarray, np.ndarray]:
        '''Prepare data for fitting or predicting.'''
        raise NotImplementedError

    @abc.abstractmethod
    def _standardize_y(self, y: np.ndarray) -> np.ndarray:
        '''Regularize the target values.'''
        raise NotImplementedError

    @abc.abstractmethod
    def _objective_with_gradient(
        self, x: np.ndarray, y: np.ndarray, v_old: np.ndarray,
        l2: np.float64, _lambda: np.float64, omega: np.float64,
        k: int) -> Tuple[Callable[[np.ndarray], np.float64],
                         Callable[[np.ndarray], np.ndarray]]:
        '''Return the objective function and its gradient.'''
        raise NotImplementedError

    @abc.abstractmethod
    def _yhat(self, x: np.ndarray) -> np.ndarray:
        '''Return the predicted values as an np.ndarray.'''
        raise NotImplementedError

    def _fit(self, dataset: Optional[Dataset], **kwargs) -> None:
        '''Fit a model based on train data.

        This sets self.trained to True.
        '''
        try:
            np_cov, np_tar = self._prepare_data(dataset)
        except NoDataError:
            return  # There is nothing to do.

        logger.debug('Fitting %s; dataset: %r, len(neighbor_models): %s',
                     type(self).__name__, dataset, len(list(self._neighbor_models_iter)))
        x = np_cov
        _, d = x.shape

        # If we have neither data nor neighbors, there's nothing to do.
        if dataset is None and not list(self._neighbor_models_iter):
            return

        omega = self._omega
        _lambda = self._lambda

        assert self._my_state is not None, (
            'BUG: self._my_state should not be None when _fit is called.'
        )
        assert isinstance(self._my_state, LinearNeighborState), (
            'BUG: expected self._my_state to be a LinearNeighborState, '
            f'instead found {self._my_state} of type {type(self._my_state)}'
        )
        y = self._standardize_y(np_tar)
        k = len(self._neighbor_models)

        # get v_old (v from last fit) if it exists or set it to 0
        v_old = np.zeros(d) if self._my_state.v.size != d else self._my_state.v.copy()
        l2 = self._l2
        fun, jac = self._objective_with_gradient(
            x=x, y=y, v_old=v_old, l2=l2, _lambda=_lambda, omega=omega, k=k)
        x0 = self._my_state.v if self._my_state is not None else np.zeros(d)
        soln = minimize(fun, x0, method='BFGS', jac=jac)
        self._my_state.v = soln.x
        logger.debug('%s fit complete; v: %r', type(self).__name__, self._my_state.v)

    def _predict(self, dataset: Optional[Dataset], **kwargs) -> Optional[Dataset]:
        '''Apply model to input dataset to create output.

        This may require that the model is fit (self.trained == True) before it is called.
        '''
        assert self._my_state is not None, (
            'BUG: self._my_state should not be None when predict is called.'
        )
        assert isinstance(self._my_state, LinearNeighborState), (
            'BUG: expected self._my_state to be a LinearNeighborState, '
            f'instead found {self._my_state} of type {type(self._my_state)}'
        )

        if dataset is None:
            return None

        x = self._prepare_data(dataset)[0]

        yhat = self._yhat(x)

        retval = dataset.output()
        # TODO(Piggy/Merritt): Convert to picard format.
        #   Preserve the column names as class names
        #   Other classification algorithms should follow the
        #   format of one column per class with probabilities
        #   for that class.
        target_col_name = dataset.metadata.roles[RoleName.TARGET][0].name
        if self._yhat_is_proba:
            retval.probabilities = pd.DataFrame(yhat)

            pred_df = pd.DataFrame({
                target_col_name: np.argmax(yhat, axis=1)
            })
        else:
            pred_df = pd.DataFrame({
                target_col_name: yhat
            })
        retval.predictions = pred_df
        return retval

    @property
    def coef(self) -> np.ndarray:
        '''Weights for the model.'''
        assert self._my_state is not None
        assert isinstance(self._my_state, LinearNeighborState)
        return self._my_state.v[:-1].copy()

    @property
    def intercept(self) -> np.float64:
        '''Intercept for the model.'''
        assert self._my_state is not None
        assert isinstance(self._my_state, LinearNeighborState)
        return self._my_state.v[-1]

    @property
    def params(self) -> np.ndarray:
        '''All the params for the model.'''
        assert self._my_state is not None
        assert isinstance(self._my_state, LinearNeighborState)
        return self._my_state.v
