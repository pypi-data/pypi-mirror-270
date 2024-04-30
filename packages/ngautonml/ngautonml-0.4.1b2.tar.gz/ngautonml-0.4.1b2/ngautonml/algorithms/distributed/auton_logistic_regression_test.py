'''Tests for auton_lr.py'''

# Copyright (c) 2024 Carnegie Mellon University
# This code is subject to the license terms contained in the LICENSE file.

# pylint: disable=missing-function-docstring, duplicate-code, protected-access

from copy import deepcopy
import pickle
import socket
import time
from typing import Tuple

import numpy as np
import pandas as pd
import pytest
from sklearn import datasets  # type: ignore[import]


from ..impl.algorithm_auto import AlgorithmCatalogAuto

from ...config_components.distributed_config import DistributedConfig
from ...metrics.impl.metric_auto import MetricCatalogAuto
from ...problem_def.task import TaskType
from ...wrangler.base_port import BasePort
from ...wrangler.dataset import Column, Dataset, Metadata, RoleName
from .auton_logistic_regression import (
    AutonLogisticRegression, AutonLogisticRegressionInstance, AutonLogisticRegressionNeighbor)


# from ...wrangler.logger import Logger
# _ = Logger(__file__, only_if_filepath_contains='distributed_algorithm_instance.py')

base_port = BasePort(7400)


CORRECT_V = np.array([-0.5086, 2.3477, -0.2656, 19.2694])

CORRECT_V_L2 = 10.0
CORRECT_DIST_PARAMS = {
    'L2': CORRECT_V_L2,
    'Lambda': 100,
    'omega': 0.6
}
CORRECT_V_ACC = 0.86
GOOD_ENOUGH_ACC = 0.85


def load_classification_dataset() -> Tuple[Dataset, Dataset, Dataset, Dataset]:
    # Load the breast cancer dataset
    bc_x_full, bc_y_series = datasets.load_breast_cancer(return_X_y=True, as_frame=True)
    assert isinstance(bc_x_full, pd.DataFrame)
    assert isinstance(bc_y_series, pd.Series)
    bc_y = pd.DataFrame({'target': bc_y_series})

    # restrict number of attributes for wider variability of results
    bc_x = bc_x_full.iloc[:, :3]

    test_size = 50
    # Split the data into training/testing sets
    bc_x_train = bc_x[:-test_size]
    bc_x_test = bc_x[-test_size:]

    # Split the targets into training/testing sets
    bc_y_train = bc_y[:-test_size]
    bc_y_test = bc_y[-test_size:].reset_index()

    metadata = Metadata(
        roles={RoleName.TARGET: [Column('target')]},
        task=TaskType.BINARY_CLASSIFICATION
    )

    dataset_train = Dataset(
        metadata=metadata,
        covariates=bc_x_train,
        target=bc_y_train
    )

    dataset_test = Dataset(
        metadata=metadata,
        covariates=bc_x_test
    )
    ground_truth = Dataset(
        metadata=metadata,
        ground_truth=bc_y_test
    )

    train_cov_0 = dataset_train['covariates'][np.array(dataset_train['target']) == 0]
    train_cov_1 = dataset_train['covariates'][np.array(dataset_train['target']) == 1]
    reduced_train = Dataset(
        covariates=pd.concat((train_cov_0.iloc[0:1], train_cov_1.iloc[0:1]), axis=0) * 0,
        target=pd.DataFrame({'target': [0] * 1 + [1] * 1}),
        metadata=metadata
    )

    return (dataset_train, dataset_test, ground_truth, reduced_train)


LOOPBACK = '127.0.0.1'
SUNNY_DAY_PORT = base_port.next()


def test_sunny_day() -> None:
    '''Sunny day with no neighbors produces the same result as sklearn.'''
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

    sklearn_alg = AlgorithmCatalogAuto().lookup_by_name('sklearn.linear_model.LogisticRegression')
    alg = AutonLogisticRegression()

    # Setting Lambda and L2 values to make our results similar to
    #   sklearn's logistic regression, in order to be more certain
    #   that our algorithm is reasonable.
    dut = alg.instantiate(
        distributed=distributed_config,
        L2=CORRECT_V_L2)
    assert isinstance(dut, AutonLogisticRegressionInstance)

    sklearn_dut = sklearn_alg.instantiate(
        C=1 / CORRECT_V_L2,
        penalty='l2',
        fit_intercept=True,
    )

    metric_catalog = MetricCatalogAuto()
    metric = metric_catalog.lookup_by_name('accuracy_score')

    train, test, ground_truth, _ = load_classification_dataset()

    try:
        dut.start()
        dut.fit(train)
        sklearn_dut.fit(train)

        sklearn_dut_v = np.array(list(sklearn_dut.impl.coef_.ravel())
                                 + [sklearn_dut.impl.intercept_[0]])
        dut_v = dut.params

        print("DEBUG,  dut_v = ", list(dut_v))
        print("DEBUG,  sklearn_dut_v = ", list(sklearn_dut_v))

        result_train = dut.predict(train)
        sklearn_result_train = sklearn_dut.predict(train)
        sklearn_train_acc = metric.calculate(
            pred=sklearn_result_train,
            ground_truth=Dataset(metadata=train.metadata, ground_truth=train['target']))
        result_train_acc = metric.calculate(
            pred=result_train,
            ground_truth=Dataset(metadata=train.metadata, ground_truth=train['target']))

        assert result_train_acc == pytest.approx(expected=sklearn_train_acc, abs=0.01)

        result_test = dut.predict(test)
        sklearn_result_test = sklearn_dut.predict(test)
        sklearn_test_acc = metric.calculate(pred=sklearn_result_test,
                                            ground_truth=ground_truth)
        result_test_acc = metric.calculate(pred=result_test,
                                           ground_truth=ground_truth)

        assert result_test_acc == pytest.approx(expected=sklearn_test_acc, abs=0.01)
        assert result_test_acc == CORRECT_V_ACC

    finally:
        dut.stop()


RECEIVE_EVENT_SENDER_PORT = base_port.next()
RECEIVE_EVENT_RECEIVER_PORT = base_port.next()


def test_receive_event() -> None:
    '''Poor training is improved with information from a neighbor.'''
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
    metric = metric_catalog.lookup_by_name('accuracy_score')

    _, test, ground_truth, reduced_train = load_classification_dataset()

    dut = AutonLogisticRegression().instantiate(distributed=distributed_config)

    sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
    sock.bind((LOOPBACK, RECEIVE_EVENT_SENDER_PORT))

    # These parameters were hand-extracted from a successful fit.
    message = pickle.dumps((
        1,
        CORRECT_V
    ))

    try:
        dut.start()
        dut.fit(reduced_train)

        check = dut.predict(test)

        # Confirm that the training is very bad.
        assert metric.calculate(pred=check,
                                ground_truth=ground_truth
                                ) == pytest.approx(expected=0.2, abs=0.01)

        sock.sendto(message, (LOOPBACK, RECEIVE_EVENT_RECEIVER_PORT))

        # Wait for the message to arrive and get processed.
        time.sleep(1.0)

        dut.fit(reduced_train)  # fit again on same data to incorporate info from neighbor

        # Confirm that we learned from our neighbor.
        got = dut.predict(test)

        assert metric.calculate(pred=got,
                                ground_truth=ground_truth
                                ) > GOOD_ENOUGH_ACC
    finally:
        dut.stop()
        sock.close()


SEND_SENDER_PORT = base_port.next()
SEND_RECEIVER_PORT = base_port.next()


def test_send() -> None:
    '''We share our coefficients with a neighbor.'''
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
                    ('1', (LOOPBACK, SEND_SENDER_PORT)),
                    ('2', (LOOPBACK, SEND_RECEIVER_PORT)),
                ],
            },
        },
        'my_id': 1,
    })

    train, _, _, _ = load_classification_dataset()

    receiver = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
    receiver.bind((LOOPBACK, SEND_RECEIVER_PORT))
    dut = None

    try:
        dut = AutonLogisticRegression().instantiate(distributed=distributed_config)
        dut.start()
        dut.fit(train)

        got_raw = receiver.recv(1024)  # Wait for the message to arrive and get processed.
        got = AutonLogisticRegressionNeighbor.decode(got_raw)

        print("DEBUG,  got.v = ", list(got.v))
        assert got.v == pytest.approx(CORRECT_V, abs=0.001)

    finally:
        receiver.close()
        if dut is not None:
            dut.stop()


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
    metric = metric_catalog.lookup_by_name('accuracy_score')

    train, test, ground_truth, _ = load_classification_dataset()

    distributed_receiver_clause = deepcopy(distributed_clause)
    distributed_receiver_clause['my_id'] = 1
    distributed_sender_clause = deepcopy(distributed_clause)
    distributed_sender_clause['my_id'] = 2

    alg = AutonLogisticRegression()
    dut_receiver = alg.instantiate(
        distributed=DistributedConfig(distributed_receiver_clause),
        **CORRECT_DIST_PARAMS)
    dut_sender = None
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
                                ) == CORRECT_V_ACC

        assert metric.calculate(pred=got_sender,
                                ground_truth=ground_truth
                                ) == CORRECT_V_ACC

        assert got_receiver is not None
        assert got_sender is not None

        pd.testing.assert_frame_equal(got_receiver.predictions, got_sender.predictions)

        assert dut_sender.params == pytest.approx(dut_receiver.params, abs=0.001)

    finally:
        dut_receiver.stop()
        if dut_sender is not None:
            dut_sender.stop()


INTEGRATED_RECEIVER_PORT = base_port.next()
INTEGRATED_SENDER_PORT = base_port.next()


def test_integrated() -> None:
    ''''Two nodes talking to each other.

    One gets poor taining, the other gets full training.
    We see that both nodes eventually get good results.
    '''
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
                    ('1', (LOOPBACK, INTEGRATED_RECEIVER_PORT)),
                    ('2', (LOOPBACK, INTEGRATED_SENDER_PORT)),
                ]
            }
        },
        'my_id': 0,
    }

    metric_catalog = MetricCatalogAuto()
    metric = metric_catalog.lookup_by_name('accuracy_score')

    train, test, ground_truth, reduced_train = load_classification_dataset()
    # TODO(Dan) Catch the case where there is only 1 class in the training data.
    distributed_receiver_clause = deepcopy(distributed_clause)
    distributed_receiver_clause['my_id'] = 1
    distributed_sender_clause = deepcopy(distributed_clause)
    distributed_sender_clause['my_id'] = 2

    alg = AutonLogisticRegression()
    receiver = alg.instantiate(
        distributed=DistributedConfig(distributed_receiver_clause),
        **CORRECT_DIST_PARAMS)

    dut = None
    try:
        receiver.start()
        receiver.fit(reduced_train)

        check = receiver.predict(test)

        print("DEBUG, receiver.params = ", list(receiver.params))

        # Confirm that the training is bad.
        assert metric.calculate(pred=check,
                                ground_truth=ground_truth
                                ) < 0.8

        dut = alg.instantiate(
            distributed=DistributedConfig(distributed_sender_clause),
            **CORRECT_DIST_PARAMS)
        dut.start()
        dut.fit(train)

        # Wait for the message to arrive and get processed.
        time.sleep(1.0)

        got = receiver.predict(test)

        # Actually 0.98! Is this a bug? It's better than the non-distributed result.
        assert metric.calculate(pred=got,
                                ground_truth=ground_truth
                                ) > GOOD_ENOUGH_ACC
    finally:
        receiver.stop()
        if dut is not None:
            dut.stop()


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

    metric_catalog = MetricCatalogAuto()
    metric = metric_catalog.lookup_by_name('accuracy_score')

    train, test, ground_truth, _ = load_classification_dataset()
    print("DEBUG : train['covariates'].shape[0] = ", train['covariates'].shape[0])
    n = train['covariates'].shape[0]
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
    dist_params_first.update(
        L2=(half_n / n) * CORRECT_DIST_PARAMS['L2'],
        Lambda=10000000)
    dist_params_second = dict(dist_params_first)
    dist_params_second.update(L2=((n - half_n) / n) * CORRECT_DIST_PARAMS['L2'])

    alg = AutonLogisticRegression()
    dut_first = alg.instantiate(
        distributed=DistributedConfig(distributed_receiver_clause),
        **dist_params_first)
    dut_second = None

    try:
        dut_first.start()
        dut_first.fit(train_first)

        dut_second = alg.instantiate(
            distributed=DistributedConfig(distributed_sender_clause),
            **dist_params_second)
        dut_second.start()
        dut_second.fit(train_second)

        # Wait for the message to arrive and get processed.
        time.sleep(3.0)

        # Confirm that neighbor optimization doesn't mess up result.
        got_receiver = dut_first.predict(test)
        got_sender = dut_second.predict(test)

        assert metric.calculate(pred=got_receiver,
                                ground_truth=ground_truth
                                ) > GOOD_ENOUGH_ACC

        assert metric.calculate(pred=got_sender,
                                ground_truth=ground_truth
                                ) > GOOD_ENOUGH_ACC

        assert got_receiver is not None
        assert got_sender is not None
        pd.testing.assert_frame_equal(got_receiver.predictions, got_sender.predictions)

        assert dut_second.params == pytest.approx(dut_first.params, rel=0.01)

    finally:
        dut_first.stop()
        if dut_second is not None:
            dut_second.stop()


NO_FIT_RECEIVER_PORT = base_port.next()
NO_FIT_SENDER_PORT = base_port.next()


def test_receive_no_fit() -> None:
    '''Test that we spontaneously fit on a message from a neighbor without having seen data.'''
    distributed_config = DistributedConfig(clause={
        'polling_interval': '0.2',
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
    metric = metric_catalog.lookup_by_name('accuracy_score')

    _, test, ground_truth, _ = load_classification_dataset()

    dut = AutonLogisticRegression().instantiate(distributed=distributed_config)
    sorted_ground_truth = dut._sort_columns(ground_truth)

    sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
    sock.bind((LOOPBACK, NO_FIT_SENDER_PORT))

    # These parameters were hand-extracted from a successful fit.
    message = pickle.dumps((
        1,
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
                                ground_truth=sorted_ground_truth
                                ) > GOOD_ENOUGH_ACC
    finally:
        dut.stop()
        sock.close()


CONFLICT_RECEIVER_PORT = base_port.next()
CONFLICT_SENDER_PORT = base_port.next()


def test_node_id_conflict_ok() -> None:
    '''Nodes don't need to agree about which node has which ID.

    In this test, both nodes think they are Node 1.
    '''
    distributed_clause = {
        'polling_interval': '0.1',
        'communicator': {
            'name': 'sockets',
            'sockets': {
                'nodes_and_endpoints': [
                ]
            }
        },
        'my_id': 1,  # This is the same for both nodes.
    }

    receiver_clause = deepcopy(distributed_clause)
    assert isinstance(receiver_clause['communicator'], dict)  # to make mypy happy
    assert isinstance(receiver_clause['communicator']['sockets'], dict)  # to make mypy happy
    receiver_clause['communicator']['sockets']['nodes_and_endpoints'] = [
        ('1', (LOOPBACK, CONFLICT_RECEIVER_PORT))
    ]
    receiver_clause['discoverer'] = {
        'name': 'dynamic'
    }

    sender_clause = deepcopy(distributed_clause)
    assert isinstance(sender_clause['communicator'], dict)  # to make mypy happy
    assert isinstance(sender_clause['communicator']['sockets'], dict)  # to make mypy happy
    sender_clause['communicator']['sockets']['nodes_and_endpoints'] = [
        ('1', (LOOPBACK, CONFLICT_SENDER_PORT)),
        ('2', (LOOPBACK, CONFLICT_RECEIVER_PORT))
    ]
    sender_clause['discoverer'] = {
        'name': 'static',
        'static': {
            'adjacency': {
                '1': [2],
            }
        }
    }

    receiver_config = DistributedConfig(receiver_clause)
    sender_config = DistributedConfig(sender_clause)

    metric_catalog = MetricCatalogAuto()
    metric = metric_catalog.lookup_by_name('accuracy_score')

    train, test, ground_truth, _ = load_classification_dataset()
    reduced_train = Dataset({
        'covariates': train['covariates'].iloc[516:517] * 0,
        'target': train['target'].iloc[516:517]
    }, metadata=train.metadata)

    alg = AutonLogisticRegression()
    receiver = alg.instantiate(distributed=receiver_config)
    sender = None
    try:
        receiver.start()
        receiver.fit(reduced_train)

        check = receiver.predict(test)

        # Confirm that the training is very bad.
        assert metric.calculate(pred=check,
                                ground_truth=ground_truth
                                ) == pytest.approx(expected=0.8, abs=0.01)

        sender = alg.instantiate(distributed=sender_config)
        sender.start()
        sender.fit(train)

        # Wait for the message to arrive and get processed.
        time.sleep(1.0)

        # Confirm that we learned from our neighbor.
        got = receiver.predict(test)

        assert metric.calculate(pred=got,
                                ground_truth=ground_truth
                                ) > 0.8
    finally:
        receiver.stop()
        if sender is not None:
            sender.stop()


# UNUSED TEST (MULTICLASS) --------------------------------------


def load_multiclass_dataset() -> Tuple[Dataset, Dataset, Dataset]:
    # Load the iris dataset
    bc_x_full, bc_y_series = datasets.load_iris(return_X_y=True, as_frame=True)
    assert isinstance(bc_x_full, pd.DataFrame)
    assert isinstance(bc_y_series, pd.Series)
    bc_y = pd.DataFrame({'target': bc_y_series})

    # restrict number of attributes for wider variability of results
    bc_x = bc_x_full.iloc[:, :3]

    # shuffle our data
    bc_x = bc_x.sample(frac=1, random_state=1701)
    bc_y = bc_y.sample(frac=1, random_state=1701)

    test_size = 50
    # Split the data into training/testing sets
    bc_x_train = bc_x[:-test_size]
    bc_x_test = bc_x[-test_size:]

    # Split the targets into training/testing sets
    bc_y_train = bc_y[:-test_size]
    bc_y_test = bc_y[-test_size:]

    metadata = Metadata(
        roles={RoleName.TARGET: [Column('target')]},
        task=TaskType.BINARY_CLASSIFICATION
    )

    dataset_train = Dataset(
        metadata=metadata,
        covariates=bc_x_train,
        target=bc_y_train
    )

    dataset_test = Dataset(
        metadata=metadata,
        covariates=bc_x_test
    )
    ground_truth = Dataset(
        metadata=metadata,
        ground_truth=bc_y_test
    )
    return (dataset_train, dataset_test, ground_truth)


@pytest.mark.skip(reason="suspected in tests hanging")
def test_multiclass() -> None:
    '''LR does not currently support multiclass'''
    alg = AutonLogisticRegression()
    dut = alg.instantiate()

    metric_catalog = MetricCatalogAuto()
    metric = metric_catalog.lookup_by_name('mean_squared_error')

    train, test, ground_truth = load_multiclass_dataset()
    try:
        dut.start()
        dut.fit(train)

        result = dut.predict(test)
        assert metric.calculate(pred=result,
                                ground_truth=ground_truth
                                ) == pytest.approx(expected=0.8, abs=0.1)
    finally:
        dut.stop()
