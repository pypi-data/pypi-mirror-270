'''tests for distributed_config.py'''

# Copyright (c) 2024 Carnegie Mellon University
# This code is subject to the license terms contained in the LICENSE file.

# pylint: disable=missing-function-docstring

import pytest

from ..neighbor_manager.node_id import NodeID

from .impl.config_component import ValidationErrors
from .distributed_config import DistributedConfig

# pylint: disable=duplicate-code


def test_get_static_adjacency() -> None:
    dut = DistributedConfig(clause={
        'discoverer': {
            'name': 'static',
            'static': {
                'adjacency': {
                    '1': [2, 4, 5],
                    '2': [1, 3, 5],
                    '3': [5, 2],
                    '4': [1],
                    '5': [1, 2, 3]
                }
            }
        }
    })

    static_adjacency = dut.get_static_adjacency(my_id=NodeID(3))
    assert static_adjacency is not None
    assert set(static_adjacency) == {NodeID(2), NodeID(5)}


def test_get_static_from_edges() -> None:
    dut = DistributedConfig(clause={
        'discoverer': {
            'name': 'static',
            'static': {
                'edges': [
                    [1, 2],
                    [1, 4],
                    [1, 5],
                    [2, 3],
                    [2, 5],
                    [3, 5]
                ]
            }
        }
    })

    assert dut.get_static_adjacency(my_id=NodeID(3)) == [NodeID(2), NodeID(5)]


def test_validation_edges_wrong_length() -> None:
    dut = DistributedConfig(clause={
        'discoverer': {
            'name': 'static',
            'static': {
                'edges': [
                    [1, 2],
                    [1, 4],
                    [1, 5],
                    [2, 3],
                    [2, 5],
                    [3, 5, 7]
                ]
            }
        }
    })
    with pytest.raises(ValidationErrors, match=r'\[3, 5, 7\]'):
        dut.validate()
