'''Tests for linear_distributed_algorithm_instance.py'''

from typing import Any, Optional, Tuple
import numpy as np
import pandas as pd
import pytest

from ...config_components.distributed_config import DistributedConfig
from ...wrangler.dataset import Dataset, Metadata

from .distributed_algorithm_instance import NeighborState
from .fake_algorithm import FakeAlgorithm, FakeInstance
from .linear_distributed_algorithm_instance import (
    LinearNeighborState, LinearDistributedAlgorithmInstance)


# pylint: disable=protected-access

class FakeLinearNeighborState(LinearNeighborState):
    '''A fake neighbor state for testing.'''

    def should_send(self, distributed, last_state_sent):
        '''Determine whether to send an update to the neighbors.'''
        return True

    def encode(self) -> bytes:
        '''Encode message for distributed neighbors.'''
        return b'fake message'

    @classmethod
    def decode(cls, serialized_model: bytes) -> Any:
        '''Decode a message from a neighbor.'''
        return FakeLinearNeighborState(np.array([1, 2, 3]))


class FakeLinearDistributedAlgorithmInstance(LinearDistributedAlgorithmInstance, FakeInstance):
    '''A fake distributed linear algorithm instance for testing.'''

    def __init__(self, parent, distributed):
        super().__init__(parent, distributed)
        self._my_state = FakeLinearNeighborState(np.array([1, 2, 3]))
        self._lambda = 0.1
        self._l2 = 0.2
        self._omega = 0.3

    def _decode(self, serialized_model: bytes) -> NeighborState:
        return FakeLinearNeighborState(np.array([1, 2, 3]))

    def _objective_with_gradient(self, x, y, v_old, l2, _lambda, omega, k):
        '''Return the objective function and its gradient.'''
        def fun(v):
            _ = v
            return 0.0

        def grad(v):
            return np.zeros_like(v)

        return fun, grad

    def _prepare_data(self, dataset: Optional[Dataset]) -> Tuple[np.ndarray, np.ndarray]:
        return (np.array([[1, 2, 3], [4, 5, 6]]), np.array([7, 8, 9]))

    def _standardize_y(self, y: np.ndarray) -> np.ndarray:
        return y

    def _yhat(self, x: np.ndarray) -> np.ndarray:
        return x

    @property
    def _yhat_is_proba(self) -> bool:
        return False


class FakeLinearDistributedAlgorthm(FakeAlgorithm):
    '''A fake distributed linear algorithm for testing.'''
    _name = 'fake_distributed_linear_algorithm'

    _default_hyperparams = {
        'Lambda': 0.1,
        'L2': 0.2,
        'omega': 0.3
    }

    def instantiate(self, **hyperparams) -> FakeInstance:
        return FakeLinearDistributedAlgorithmInstance(parent=self, **hyperparams)


def test_sort_columns():
    '''Test _sort_columns.'''
    config = DistributedConfig({})
    dut = FakeLinearDistributedAlgorthm().instantiate(distributed=config)
    assert isinstance(dut, FakeLinearDistributedAlgorithmInstance)
    input_df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [4, 5, 6],
        'c': [7, 8, 9]})

    input_df = input_df.reindex(columns=['c', 'b', 'a'])
    want_df = input_df.reindex(columns=['a', 'b', 'c'])

    input_covariates_df = input_df[['c', 'b']]
    want_covariates_df = input_covariates_df.reindex(columns=['b', 'c'])

    # Confirm that it matters that the columns are out of order.
    with pytest.raises(AssertionError):
        pd.testing.assert_frame_equal(input_df, want_df)

    input_dataset = Dataset(dataframe=input_df,
                            covariates=input_covariates_df,
                            target=input_df['a'],
                            metadata=Metadata(
                                roles={'target': ['a']}))

    got = dut._sort_columns(input_dataset)

    pd.testing.assert_frame_equal(got['dataframe'], want_df)
    pd.testing.assert_frame_equal(got['covariates'], want_covariates_df)
