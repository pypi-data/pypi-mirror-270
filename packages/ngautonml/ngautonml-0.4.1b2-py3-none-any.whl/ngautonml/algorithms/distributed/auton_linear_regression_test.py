'''Tests for auton_linear_regression.py'''

# Copyright (c) 2024 Carnegie Mellon University
# This code is subject to the license terms contained in the LICENSE file.

# pylint: disable=missing-function-docstring,duplicate-code

from copy import deepcopy
import pickle
import socket
import time
from typing import Tuple

import numpy as np
import pandas as pd
import pytest
from sklearn import datasets  # type: ignore[import]

from ...algorithms.impl.algorithm_auto import AlgorithmCatalogAuto
from ...config_components.distributed_config import DistributedConfig
from ...metrics.impl.metric_auto import MetricCatalogAuto
from ...wrangler.base_port import BasePort  # type: ignore[import]
from ...wrangler.dataset import Column, Dataset, Metadata, RoleName
from .auton_linear_regression import (
    AutonLinearRegression,
    AutonLinearRegressionInstance,
    AutonLinearRegressionNeighbor)


CORRECT_V_L2 = 10
CORRECT_V = np.array([
    19.80426349, -1.23138257, 71.81414651,
    52.85306555, 19.89796648, 14.13228464, -45.26142198,
    47.34059162, 67.39734652, 43.43461662, 153.30386624])
CORRECT_V_MSE = 4436.62
BAD_MSE = 5000
CORRECT_DIST_PARAMS = {
    'L2': CORRECT_V_L2,
    'Lambda': 10000000000,
    'omega': 2.0 / 3.0
}


def load_regression_dataset() -> Tuple[Dataset, Dataset, Dataset, Dataset]:
    # Load the diabetes dataset
    diabetes_x, diabetes_y = datasets.load_diabetes(return_X_y=True)

    # Use only one feature
    # diabetes_x = diabetes_x[:, np.newaxis, 2]

    # Split the data into training/testing sets
    diabetes_x_train = diabetes_x[:-20]
    diabetes_x_test = diabetes_x[-20:]

    # Split the targets into training/testing sets
    diabetes_y_train = diabetes_y[:-20]
    diabetes_y_test = diabetes_y[-20:]
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    metadata = Metadata(roles={RoleName.TARGET: [Column('target')]})
    dataset_train = Dataset(
        metadata=metadata,
        covariates=pd.DataFrame(diabetes_x_train, columns=columns),
        target=pd.DataFrame({'target': diabetes_y_train})
    )
    dataset_test = Dataset(
        metadata=metadata,
        covariates=pd.DataFrame(diabetes_x_test, columns=columns)
    )
    ground_truth = Dataset(
        metadata=metadata,
        ground_truth=pd.DataFrame({'target': diabetes_y_test})
    )

    reduced_train = Dataset(
        covariates=pd.DataFrame(np.zeros((2, len(columns))), columns=columns),
        target=pd.DataFrame({'target': diabetes_y_train[:2]}),
        metadata=metadata
    )
    return (dataset_train, dataset_test, ground_truth, reduced_train)


base_port = BasePort(7340)

LOOPBACK = '127.0.0.1'
SUNNY_DAY_PORT = base_port.next()


def test_sunny_day() -> None:
    distributed_config = DistributedConfig(clause={
        'discoverer': {
            'name': 'static',
            'static': {
                'adjacency': {
                    '2': [],
                }
            }
        },
        'communicator': {
            'name': 'sockets',
            'sockets': {
                'nodes_and_endpoints': [
                    ('2', (LOOPBACK, SUNNY_DAY_PORT)),
                ]
            },
        },
        'my_id': 2,
    })

    sklearn_alg = AlgorithmCatalogAuto().lookup_by_name('sklearn.linear_model.Ridge')

    alg = AutonLinearRegression()

    # Setting Lambda and L2 values to make our results similar to
    #   sklearn's logistic regression, in order to be more certain
    #   that our algorithm is reasonable.
    dut = alg.instantiate(
        distributed=distributed_config,
        Lambda=0.0, L2=CORRECT_V_L2)
    assert isinstance(dut, AutonLinearRegressionInstance)
    sklearn_dut = sklearn_alg.instantiate(
        alpha=CORRECT_V_L2
    )

    metric_catalog = MetricCatalogAuto()
    metric = metric_catalog.lookup_by_name('mean_squared_error')

    train, test, ground_truth, _ = load_regression_dataset()

    try:
        dut.start()
        dut.fit(train)
        sklearn_dut.fit(train)

        sklearn_dut_v = np.array(list(sklearn_dut.impl.coef_) + [sklearn_dut.impl.intercept_])
        dut_v = dut.params

        result = dut.predict(test)
        sklearn_result = sklearn_dut.predict(test)

        sklearn_mse = metric.calculate(pred=sklearn_result,
                                       ground_truth=ground_truth
                                       )

        result_mse = metric.calculate(pred=result,
                                      ground_truth=ground_truth
                                      )

        assert dut_v == pytest.approx(sklearn_dut_v, abs=0.01)
        assert result_mse == pytest.approx(expected=sklearn_mse, abs=0.01)
        assert result_mse == pytest.approx(CORRECT_V_MSE, abs=0.1)
    finally:
        dut.stop()


RECEIVE_EVENT_SENDER_PORT = base_port.next()
RECEIVE_EVENT_RECEIVER_PORT = base_port.next()


def test_receive_event() -> None:
    distributed_config = DistributedConfig(clause={
        'discoverer': {
            'name': 'static',
            'static': {
                'adjacency': {
                    '1': [2],
                    '2': [1],
                },
            },
        },
        'communicator': {
            'name': 'sockets',
            'sockets': {
                'nodes_and_endpoints': [
                    ('1', (LOOPBACK, RECEIVE_EVENT_SENDER_PORT)),
                    ('2', (LOOPBACK, RECEIVE_EVENT_RECEIVER_PORT)),
                ],
            },
        },
        'my_id': 2,
    })

    metric_catalog = MetricCatalogAuto()
    metric = metric_catalog.lookup_by_name('mean_squared_error')

    _, test, ground_truth, reduced_train = load_regression_dataset()

    dut = AutonLinearRegression().instantiate(distributed=distributed_config, **CORRECT_DIST_PARAMS)

    sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
    sock.bind((LOOPBACK, RECEIVE_EVENT_SENDER_PORT))

    # These parameters were hand-extracted from a successful fit.
    message = pickle.dumps(
        CORRECT_V
    )

    try:
        dut.start()
        dut.fit(reduced_train)

        got_reduced = dut.predict(test)

        reduced_metric = metric.calculate(pred=got_reduced,
                                          ground_truth=ground_truth
                                          )
        assert reduced_metric > BAD_MSE

        sock.sendto(message, (LOOPBACK, RECEIVE_EVENT_RECEIVER_PORT))

        # Wait for the message to arrive and get processed.
        time.sleep(1.0)

        # Confirm that we learned from our neighbor.
        got = dut.predict(test)

        assert metric.calculate(pred=got,
                                ground_truth=ground_truth
                                ) < reduced_metric - 50
    finally:
        dut.stop()
        sock.close()


SEND_SENDER_PORT = base_port.next()
SEND_RECEIVER_PORT = base_port.next()


def test_send() -> None:
    distributed_config = DistributedConfig(clause={
        'polling_interval': '1.0',  # formerly 0.1
        'discoverer': {
            'name': 'static',
            'static': {
                'adjacency': {
                    '1': [2],
                    '2': [1],
                }
            }
        },
        'communicator': {
            'name': 'sockets',
            'sockets': {
                'nodes_and_endpoints': [
                    ('1', (LOOPBACK, SEND_SENDER_PORT)),
                    ('2', (LOOPBACK, SEND_RECEIVER_PORT)),
                ],
            },
        },
        'my_id': 1,
    })

    train, _, _, _ = load_regression_dataset()

    receiver = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
    receiver.bind((LOOPBACK, SEND_RECEIVER_PORT))

    try:
        dut = AutonLinearRegression().instantiate(distributed=distributed_config,
                                                  **CORRECT_DIST_PARAMS)
        dut.start()
        dut.fit(train)

        got_raw = receiver.recv(1024)  # Wait for the message to arrive and get processed.
        got = AutonLinearRegressionNeighbor.decode(got_raw)

        assert got.v == pytest.approx(CORRECT_V, abs=0.001)

    finally:
        receiver.close()
        dut.stop()


INTEGRATED_RECEIVER_PORT = base_port.next()
INTEGRATED_SENDER_PORT = base_port.next()


def test_integrated() -> None:
    distributed_clause = {
        'polling_interval': '1.0',  # formerly 0.1
        'discoverer': {
            'name': 'static',
            'static': {
                'adjacency': {
                    '1': [2],
                    '2': [1],
                }
            }
        },
        'communicator': {
            'name': 'sockets',
            'sockets': {
                'nodes_and_endpoints': [
                    ('1', (LOOPBACK, INTEGRATED_RECEIVER_PORT)),
                    ('2', (LOOPBACK, INTEGRATED_SENDER_PORT)),
                ]
            }
        },
        'my_id': 0,
    }

    metric_catalog = MetricCatalogAuto()
    metric = metric_catalog.lookup_by_name('mean_squared_error')

    train, test, ground_truth, reduced_train = load_regression_dataset()

    distributed_receiver_clause = deepcopy(distributed_clause)
    distributed_receiver_clause['my_id'] = 1
    distributed_sender_clause = deepcopy(distributed_clause)
    distributed_sender_clause['my_id'] = 2

    alg = AutonLinearRegression()
    receiver = alg.instantiate(distributed=DistributedConfig(distributed_receiver_clause),
                               **CORRECT_DIST_PARAMS)

    sender = None
    try:
        receiver.start()
        receiver.fit(reduced_train)

        check = receiver.predict(test)

        # Confirm that the training is very bad.
        assert metric.calculate(pred=check,
                                ground_truth=ground_truth
                                ) > BAD_MSE

        sender = alg.instantiate(distributed=DistributedConfig(distributed_sender_clause),
                                 **CORRECT_DIST_PARAMS)
        sender.start()
        sender.fit(train)

        # Wait for the message to arrive and get processed.
        time.sleep(1.0)

        # Confirm that we learned from our neighbor.
        got_receiver = receiver.predict(test)
        got_sender = sender.predict(test)

        assert metric.calculate(pred=got_receiver,
                                ground_truth=ground_truth
                                ) < BAD_MSE
        assert metric.calculate(pred=got_sender,
                                ground_truth=ground_truth
                                ) < BAD_MSE
    finally:
        receiver.stop()
        if sender is not None:
            sender.stop()


NO_FIT_RECEIVER_PORT = base_port.next()
NO_FIT_SENDER_PORT = base_port.next()


def test_receive_no_fit() -> None:
    '''Test that we spontaneously fit on a message from a neighbor without having seen data.'''
    distributed_config = DistributedConfig(clause={
        'discoverer': {
            'name': 'static',
            'static': {
                'adjacency': {
                    '1': [2],
                    '2': [1],
                }
            }
        },
        'communicator': {
            'name': 'sockets',
            'sockets': {
                'nodes_and_endpoints': [
                    ('1', (LOOPBACK, NO_FIT_SENDER_PORT)),
                    ('2', (LOOPBACK, NO_FIT_RECEIVER_PORT)),
                ],
            },
        },
        'my_id': 2,
    })

    metric_catalog = MetricCatalogAuto()
    metric = metric_catalog.lookup_by_name('mean_squared_error')

    _, test, ground_truth, _ = load_regression_dataset()

    dist_params = dict(CORRECT_DIST_PARAMS)
    dist_params['omega'] = 1.0  # zeros out self-regularization term

    dut = AutonLinearRegression().instantiate(distributed=distributed_config,
                                              **dist_params)

    sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
    sock.bind((LOOPBACK, NO_FIT_SENDER_PORT))

    # These parameters were hand-extracted from a successful fit.
    message = pickle.dumps((
        CORRECT_V
    ))

    try:
        dut.start()
        sock.sendto(message, (LOOPBACK, NO_FIT_RECEIVER_PORT))

        # Wait for the message to arrive and get processed.
        time.sleep(1.0)

        # Confirm that we learned from our neighbor.
        got = dut.predict(test)

        assert metric.calculate(pred=got,
                                ground_truth=ground_truth
                                ) == pytest.approx(expected=CORRECT_V_MSE, abs=0.1)
    finally:
        dut.stop()
        sock.close()


TWO_HALF_RECEIVER_PORT = base_port.next()
TWO_HALF_SENDER_PORT = base_port.next()


@pytest.mark.xfail(reason="Need to figure out to determine if nodes converged.")
def test_two_half() -> None:
    '''Two nodes with half the training behaves as (reasonably) expected.'''
    distributed_clause = {
        'discoverer': {
            'name': 'static',
            'static': {
                'adjacency': {
                    '1': [2],
                    '2': [1],
                }
            }
        },
        'communicator': {
            'name': 'sockets',
            'sockets': {
                'nodes_and_endpoints': [
                    ('1', (LOOPBACK, TWO_HALF_RECEIVER_PORT)),
                    ('2', (LOOPBACK, TWO_HALF_SENDER_PORT)),
                ]
            }
        },
        'my_id': 0,
    }

    # metric_catalog = MetricCatalogAuto()
    # metric = metric_catalog.lookup_by_name('mean_squared_error')

    train, _, _, _ = load_regression_dataset()
    print("DEBUG : train['covariates'].shape[0] = ", train['covariates'].shape[0])
    # n = train['covariates'].shape[0]
    half_n = int(train['covariates'].shape[0] / 2)
    train_first = Dataset(
        metadata=train.metadata,
        covariates=train['covariates'].iloc[0:half_n],
        target=train['target'].iloc[0:half_n]
    )
    train_second = Dataset(
        metadata=train.metadata,
        covariates=train['covariates'].iloc[half_n:],
        target=train['target'].iloc[half_n:]
    )

    distributed_receiver_clause = deepcopy(distributed_clause)
    distributed_receiver_clause['my_id'] = 1
    distributed_sender_clause = deepcopy(distributed_clause)
    distributed_sender_clause['my_id'] = 2

    dist_params_first = dict(CORRECT_DIST_PARAMS)
    dist_params_first.update(Lambda=1000000000000)
    dist_params_second = dict(dist_params_first)

    alg = AutonLinearRegression()
    dut_first = alg.instantiate(
        distributed=DistributedConfig(distributed_receiver_clause),
        **dist_params_first)

    try:
        dut_first.start()
        dut_first.fit(train_first)

        dut_second = alg.instantiate(
            distributed=DistributedConfig(distributed_sender_clause),
            **dist_params_second)
        dut_second.start()
        dut_second.fit(train_second)

        # Wait for the message to arrive and get processed.
        time.sleep(10)

        # Confirm that neighbor optimization doesn't mess up result.
        # got_receiver = dut_first.predict(test)
        # got_sender = dut_second.predict(test)

        # assert metric.calculate(pred=got_receiver,
        #                         ground_truth=ground_truth
        #                         ) < BAD_MSE

        # assert metric.calculate(pred=got_sender,
        #                         ground_truth=ground_truth
        #                         ) < BAD_MSE
        a = 2
        assert 1 == a
        assert dut_second.params == pytest.approx(dut_first.params)

    finally:
        dut_first.stop()
        dut_second.stop()


TWO_SAME_RECEIVER_PORT = base_port.next()
TWO_SAME_SENDER_PORT = base_port.next()


def test_two_same() -> None:
    '''Two nodes with the same training don't change their coefficients.'''
    distributed_clause = {
        'discoverer': {
            'name': 'static',
            'static': {
                'adjacency': {
                    '1': [2],
                    '2': [1],
                }
            }
        },
        'communicator': {
            'name': 'sockets',
            'sockets': {
                'nodes_and_endpoints': [
                    ('1', (LOOPBACK, TWO_SAME_RECEIVER_PORT)),
                    ('2', (LOOPBACK, TWO_SAME_SENDER_PORT)),
                ]
            }
        },
        'my_id': 0,
    }

    metric_catalog = MetricCatalogAuto()
    metric = metric_catalog.lookup_by_name('mean_squared_error')

    train, test, ground_truth, _ = load_regression_dataset()

    distributed_receiver_clause = deepcopy(distributed_clause)
    distributed_receiver_clause['my_id'] = 1
    distributed_sender_clause = deepcopy(distributed_clause)
    distributed_sender_clause['my_id'] = 2

    alg = AutonLinearRegression()
    dut_receiver = alg.instantiate(
        distributed=DistributedConfig(distributed_receiver_clause),
        **CORRECT_DIST_PARAMS)

    try:
        dut_receiver.start()
        dut_receiver.fit(train)

        dut_sender = alg.instantiate(
            distributed=DistributedConfig(distributed_sender_clause),
            **CORRECT_DIST_PARAMS)
        dut_sender.start()
        dut_sender.fit(train)

        # Wait for the message to arrive and get processed.
        time.sleep(1.0)

        # Confirm that neighbor optimization doesn't mess up result.
        got_receiver = dut_receiver.predict(test)
        got_sender = dut_sender.predict(test)

        assert metric.calculate(pred=got_receiver,
                                ground_truth=ground_truth
                                ) == pytest.approx(CORRECT_V_MSE, abs=0.1)

        assert metric.calculate(pred=got_sender,
                                ground_truth=ground_truth
                                ) == pytest.approx(CORRECT_V_MSE, abs=0.1)

        assert got_receiver is not None
        assert got_sender is not None

        pd.testing.assert_frame_equal(got_receiver.predictions, got_sender.predictions)

        assert dut_sender.params == pytest.approx(dut_receiver.params, abs=0.001)
        assert dut_sender.params == pytest.approx(CORRECT_V, abs=0.001)

    finally:
        dut_receiver.stop()
        dut_sender.stop()
