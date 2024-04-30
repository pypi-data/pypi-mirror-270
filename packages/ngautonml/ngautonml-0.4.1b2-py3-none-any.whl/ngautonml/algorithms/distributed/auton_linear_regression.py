'''Distributed Linear Regression'''

# Copyright (c) 2024 Carnegie Mellon University
# This code is subject to the license terms contained in the LICENSE file.

# Linear and Logistic Regression have portions of identical code that should
# not be abstracted away.
# pylint: disable=duplicate-code

import pickle
from typing import Callable, Iterable, Optional, Tuple

from autograd import jacobian  # type: ignore[import]
import numpy as np


from ...catalog.catalog import upcast
from ...problem_def.task import DataType, TaskType
from ...wrangler.dataset import Dataset, DatasetKeys, RoleName
from ...wrangler.logger import Logger

from ..impl.algorithm import Algorithm, MemoryAlgorithmCatalog
from ..impl.distributed_algorithm_instance import NoDataError
from ..impl.linear_distributed_algorithm_instance import (
    LinearDistributedAlgorithmInstance, LinearNeighborState,
    norm2, inner_product)


logger = Logger(__file__).logger()


class AutonLinearRegressionNeighbor(LinearNeighborState):
    '''A neighbor in the distributed linear regression model.'''

    def encode(self) -> bytes:
        '''Encode message for distributed neighbors.'''
        #  minimal: communicate as little information as possible
        return pickle.dumps(self._v)

    @classmethod
    def decode(cls, serialized_model: bytes) -> 'AutonLinearRegressionNeighbor':
        '''Decode a message from a neighbor.'''
        # minimal: communicate as little information as possible
        v = pickle.loads(serialized_model)
        assert isinstance(v, np.ndarray), (
            f'BUG: expected v to be an np.ndarray, instead found {v} of type {type(v)}'
        )
        return cls(v=v)

    @property
    def positive_class(self) -> int:
        '''The numeric identifier of the positive class in the classification problem.'''
        return self._positive_class

    @positive_class.setter
    def positive_class(self, value: int) -> None:
        '''The numeric identifier of the positive class in the classification problem.'''
        self._positive_class = value


class AutonLinearRegressionInstance(LinearDistributedAlgorithmInstance):
    '''Binary logistic regression that supports distributed AI.

    As a distributed model, this instance can share information about its
    trained state with other instances and update its trained state using
    information shared by other instances.
    '''

    # This is a type annotation for _my_state.
    _my_state: Optional[AutonLinearRegressionNeighbor] = None

    @property
    def _yhat_is_proba(self) -> bool:
        return False

    @property
    def _neighbor_models_iter(self) -> Iterable[AutonLinearRegressionNeighbor]:
        for v in super()._neighbor_models_iter:
            assert isinstance(v, AutonLinearRegressionNeighbor), (
                'BUG: expected neighbor_models to contain AutonLinearRegressionNeighbor, '
                f'instead found {v} of type {type(v)}'
            )
            yield v

    def _standardize_y(self, y: np.ndarray) -> np.ndarray:
        '''Regularize the target values.'''
        return y

    def _yhat(self, x: np.ndarray) -> np.ndarray:
        assert self._my_state is not None, (
            'BUG: self._my_state should not be None when _yhat is called.'
            ' This should have been set in _fit'
        )
        return self._my_state.v @ x.T

    def _decode(self, serialized_model: bytes) -> AutonLinearRegressionNeighbor:
        '''Decode a message from distributed neighbors.'''
        return AutonLinearRegressionNeighbor.decode(serialized_model)

    def _prepare_data(self, dataset: Optional[Dataset]) -> Tuple[np.ndarray, np.ndarray]:
        '''Extract covariates and target, accounting for the possibility that there's no data.'''
        if dataset is None:
            if list(self._neighbor_models_iter):
                d = max(len(m.v) for m in self._neighbor_models_iter) - 1
                np_cov = np.zeros((0, d))
            else:
                # TODO(Piggy/Dan) Need to figure out how to deal with no neighbors and no data.
                raise NoDataError("No data and no neighbors.")
            np_tar = np.zeros(0)
        else:
            target_col_name = dataset.metadata.roles[RoleName.TARGET][0].name
            dataset = self._sort_columns(dataset)

            if DatasetKeys.DATAFRAME.value in dataset:
                orig_cov = dataset[DatasetKeys.DATAFRAME.value].copy()
                if target_col_name in orig_cov.columns:
                    orig_cov.drop(columns=[target_col_name], inplace=True)
                    orig_tar = dataset[DatasetKeys.DATAFRAME.value].loc[:, target_col_name]
                    np_tar = orig_tar.to_numpy()
                else:
                    np_tar = np.array([0])
            else:
                orig_cov = dataset[DatasetKeys.COVARIATES.value]
                if DatasetKeys.TARGET.value in dataset:
                    orig_tar = dataset[DatasetKeys.TARGET.value]
                    np_tar = orig_tar[target_col_name].to_numpy()
                else:
                    np_tar = np.array([0])

            np_cov = orig_cov.to_numpy()

        # Add a column for the intercept.
        np_cov = np.hstack((np_cov, np.ones((np_cov.shape[0], 1))))

        _, d = np_cov.shape

        if self._my_state is None:
            self._my_state = AutonLinearRegressionNeighbor(
                v=np.zeros(d))

        return np_cov, np_tar

    def _objective_with_gradient(
            self, x: np.ndarray, y: np.ndarray, v_old: np.ndarray,
            l2: np.float64, _lambda: np.float64, omega: np.float64,
            k: int) -> Tuple[Callable[[np.ndarray], np.float64],
                             Callable[[np.ndarray], np.ndarray]]:
        '''Return the objective function and:190
          its gradient.'''

        if k > 0:
            def fun(v: np.ndarray) -> np.float64:
                data_loss = (
                    np.square(y - ((v @ x.T))).sum()
                )
                l2_regularization = l2 * norm2(v[:-1])
                neighbor_regularization = (
                    _lambda / k
                    * sum(inner_product(m.v - v, m.v - v) for m in self._neighbor_models_iter)
                )
                self_regularization = (
                    _lambda * (1 - omega) / omega * inner_product(v_old - v, v_old - v)
                )
                return (data_loss
                        + l2_regularization
                        + neighbor_regularization
                        + self_regularization)

            jac = jacobian(fun)  # pylint: disable=no-value-for-parameter

            # def jac(v: np.ndarray) -> np.ndarray:
            #     # l2_regularization = l2 * np.array(list(grad_norm2(v[:-1])) + [0])
            #     return fun_jac(v)
        else:
            def fun(v: np.ndarray) -> np.float64:
                print("DEBUG l2", l2)
                data_loss = np.square(y - (v @ x.T)).sum()
                l2_regularization = l2 * norm2(v[:-1])
                return data_loss + l2_regularization

            fun_jac = jacobian(fun)  # pylint: disable=no-value-for-parameter

            def jac(v: np.ndarray) -> np.ndarray:
                # l2_regularization = l2 * np.array(list(grad_norm2(v[:-1])) + [0])
                return fun_jac(v)

        return fun, jac


class AutonLinearRegression(Algorithm):
    '''Class for Auton Lab's implementation of Linear Regression'''
    _name = "auton_linear_regression"
    _tags = {
        'tasks': [TaskType.REGRESSION.name],
        'data_types': [DataType.TABULAR.name],
        'source': ['auton_lab'],
        'distributed': ['true']
    }
    _instance_constructor = AutonLinearRegressionInstance
    _default_hyperparams = {
        'Lambda': 100.0,  # Neighbor regularization
        'L2': 1.0,  # The normal weight regularization
        'omega': 2.0 / 3.0,  # Self regularization with last iteration's local weights
    }

    def instantiate(self, **hyperparams) -> 'AutonLinearRegressionInstance':
        return super().instantiate(**hyperparams)


def register(catalog: MemoryAlgorithmCatalog, *args, **kwargs) -> None:
    '''Register all the objects in this file.'''
    model = AutonLinearRegression(*args, **kwargs)
    catalog.register(model, model.name, upcast(model.tags))
