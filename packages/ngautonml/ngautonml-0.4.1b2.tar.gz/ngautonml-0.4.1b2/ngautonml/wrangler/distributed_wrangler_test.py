'''Tests for distributed_wrangler.py.'''

import logging
from multiprocessing import Process
import pickle
import queue
import select
import socket
import time
from typing import Optional, Tuple

import numpy as np
import pandas as pd
import pytest
import requests
from sklearn import datasets  # type: ignore[import]


from ..generator.designator import Designator
from ..instantiator.executable_pipeline import PipelineResults
from ..metrics.impl.metric_auto import MetricCatalogAuto
from ..problem_def.problem_def import ProblemDefinition
from ..wrangler.base_port import BasePort

from .distributed_wrangler import DistributedWrangler

# pylint: disable=missing-function-docstring, missing-class-docstring, duplicate-code, unused-variable
# pylint: disable=too-many-locals


base_port = BasePort(5500)


def load_classification_dataframes(
        reduced_train: bool = False) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
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
    bc_x_test = bc_x[-test_size:].reset_index(drop=True)

    # Split the targets into training/testing sets
    bc_y_train = bc_y[:-test_size]
    bc_y_test = bc_y[-test_size:].reset_index(drop=True)

    train_df = pd.concat([bc_x_train, bc_y_train], axis=1)
    test_df = bc_x_test
    gt_df = bc_y_test

    if reduced_train:
        train_df = train_df.iloc[516:519]

    return (train_df, test_df, gt_df)


LOOPBACK = '127.0.0.1'
SUNNY_DAY_RECEIVER_PORT = base_port.next()
SUNNY_DAY_SENDER_PORT = base_port.next()


def test_sunny_day() -> None:
    train_df, test_df, gt_df = load_classification_dataframes(reduced_train=True)  # noqa: F841

    pdef = ProblemDefinition(clause={
        'dataset': {
            'config': 'memory',
            'params': {
                'train_data': 'train_df',
                'test_data': 'test_df',
            },
            'column_roles': {
                'target': {'name': 'target'},
            },
        },
        'distributed': {
            'polling_interval': 0.5,
            'discoverer': {
                'name': 'static',
                'static': {
                    'adjacency': {
                        '1': [],
                    },
                },
            },
            'communicator': {
                'name': 'sockets',
                'sockets': {
                    'nodes_and_endpoints': [
                        ('1', (LOOPBACK, SUNNY_DAY_RECEIVER_PORT)),
                    ],
                },
            },
            'my_id': 1,
            'split': {
                'num_nodes': 2,
                'seed': 1234,
            },
            'pipelines': {
                'just': ['Auton_Logistic_Regression'],
            }
        },
        'problem_type': {
            'task': 'binary_classification',
        }
    })

    dut = DistributedWrangler(problem_definition=pdef)
    ground_truth = dut.dataset(data=gt_df, key='ground_truth')
    test_dataset = dut.dataset(data=test_df)

    sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
    sock.bind((LOOPBACK, SUNNY_DAY_SENDER_PORT))

    # These parameters were hand-extracted from a successful fit.
    message = pickle.dumps((
        1,
        np.array([5.72550884, 0.09525482, -0.89685941, 0.0])
    ))

    metric_catalog = MetricCatalogAuto()
    metric = metric_catalog.lookup_by_name('accuracy_score')
    try:
        dut.start()
        time.sleep(1)
        res1: Optional[PipelineResults] = dut.predict(test_dataset)
        assert res1 is not None
        assert len(res1) == 1

        # Confirm that the training is very bad.
        assert metric.calculate(pred=next(iter(res1.values())).prediction,
                                ground_truth=ground_truth
                                ) == pytest.approx(expected=0.2, abs=0.01)

        sock.sendto(message, (LOOPBACK, SUNNY_DAY_RECEIVER_PORT))

        # Wait for the message to arrive and get processed.
        time.sleep(1.0)

        res2 = dut.predict(test_dataset)
        assert res2 is not None
        assert len(res2) == 1

        # Confirm that the training is now better.
        assert metric.calculate(pred=next(iter(res2.values())).prediction,
                                ground_truth=ground_truth
                                ) >= 0.8
    finally:
        sock.close()
        dut.stop()


def test_lookup_templates() -> None:
    '''Test 3 ways of specifying pipeline loader args in the problem def.

    (single arg, multiple *args list, and **kwargs dict)
    '''
    pdef = ProblemDefinition(clause={
        'dataset': {
            'config': 'ignore'
        },
        'problem_type': {
            'task': 'test_task'
        },
        'distributed': {
            'communicator': {
                'name': 'stub_communicator'
            },
            'split': {
                'my_id': 1,
            },
            'pipelines': {
                'just': [
                    'auton_Logistic_Regression',
                    ['connect'],
                    {'alg': 'identity'}
                ]
            }
        }
    })
    dut = DistributedWrangler(problem_definition=pdef)
    dut.stop()
    got = dut.bound_pipelines
    want = {
        Designator('auton_logistic_regression'),
        Designator('connect'),
        Designator('identity'),
    }
    assert {pipe.designator for pipe in got.values()} == want


SUNNY_DAY_SERVER_MY_PORT = base_port.next()
SUNNY_DAY_SERVER_NEIGHBOR_PORT = base_port.next()
SUNNY_DAY_SERVER_WEB_PORT = base_port.next()


def test_server_sunny_day() -> None:
    '''Test the web server with a fit and predict request.'''
    train_df, test_df, gt_df = load_classification_dataframes(reduced_train=True)  # noqa: F841

    empty_df = pd.DataFrame()  # noqa: F841

    poll_queue: queue.Queue[pd.DataFrame] = queue.Queue()  # noqa: F841

    pdef = ProblemDefinition(clause={
        'dataset': {
            'config': 'ignore',
            'column_roles': {
                'target': {
                    'name': 'target',
                    'pos_label': 1,
                },
            },
        },
        'distributed': {
            'polling_interval': 0.5,
            'discoverer': {
                'name': 'static',
                'static': {
                    'adjacency': {
                        '1': ['2'],
                        '2': ['1'],
                    },
                },
            },
            'communicator': {
                'name': 'sockets',
                'sockets': {
                    'nodes_and_endpoints': [
                        ('1', (LOOPBACK, SUNNY_DAY_SERVER_MY_PORT)),
                        ('2', (LOOPBACK, SUNNY_DAY_SERVER_NEIGHBOR_PORT)),
                    ],
                },
            },
            'my_id': 1,
            'split': {
                'num_nodes': 2,
                'seed': 1234,
            },
            'pipelines': {
                'just': ['Auton_Logistic_regression'],
            }
        },
        'problem_type': {
            'task': 'binary_classification',
        }
    })

    dut = DistributedWrangler(problem_definition=pdef)

    train_msg = {
        'target': {'target': train_df['target'].tolist()},
        'covariates': train_df.drop(columns=['target']).to_dict(orient='list'),
    }

    test_msg = {
        'dataframe': test_df.to_dict(orient='list'),
    }

    # These parameters were hand-extracted from a successful fit.
    want_message = (1, [-2.35954881e-01, -3.53208883e-02, -1.47851365e-02, 2.50055077e+01])

    neighbor = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
    neighbor.bind((LOOPBACK, SUNNY_DAY_SERVER_NEIGHBOR_PORT))
    neighbor.setblocking(False)
    server = None
    exception = None
    try:
        server = Process(target=dut.server(host=LOOPBACK, port=SUNNY_DAY_SERVER_WEB_PORT))
        server.start()

        time.sleep(2.0)

        r = requests.post(f'http://localhost:{SUNNY_DAY_SERVER_WEB_PORT}/wrangler/v1.0/fit',
                          json={
                              'data': train_msg,
                          },
                          timeout=None)

        assert r.text == '{"status":"OK"}\n'

        ready = select.select([neighbor], [], [], 60.0)
        if ready[0]:
            neighbor_response = neighbor.recv(1024)
        else:
            raise TimeoutError('Timeout waiting for neighbor to respond')

        response = pickle.loads(neighbor_response)
        assert response[1] == pytest.approx(want_message[1], abs=0.01)

        r = requests.post(f'http://localhost:{SUNNY_DAY_SERVER_WEB_PORT}/wrangler/v1.0/predict',
                          json={
                              'data': test_msg,
                          },
                          timeout=None)
        got = r.json()

        assert 'auton_logistic_regression' in got

        prediction = dut.dataset(
            pd.DataFrame({'target': got['auton_logistic_regression']}),
            key='predictions')

        metric_catalog = MetricCatalogAuto()
        metric = metric_catalog.lookup_by_name('accuracy_score')
        ground_truth = dut.dataset(data=gt_df, key='ground_truth')

        assert metric.calculate(pred=prediction,
                                ground_truth=ground_truth) == pytest.approx(0.98, abs=0.01)

    except Exception as e:  # pylint: disable=broad-except
        exception = e
        logging.debug("exception %s in test_server_sunny_day", e)
    finally:
        if server is not None:
            server.terminate()
            server.join()
        neighbor.close()

    if exception is not None:
        raise exception


MY_ID_SERVER_MY_PORT = base_port.next()
MY_ID_SERVER_NEIGHBOR_PORT = base_port.next()
MY_ID_SERVER_WEB_PORT = base_port.next()


def test_server_set_my_id() -> None:
    '''Test starting the web server with a specified my_id.'''
    train_df, test_df, gt_df = load_classification_dataframes(reduced_train=True)  # noqa: F841

    pdef = ProblemDefinition(clause={
        'dataset': {
            'config': 'ignore',
            'column_roles': {
                'target': {
                    'name': 'target',
                    'pos_label': 1,
                },
            },
        },
        'distributed': {
            'polling_interval': 0.5,
            'discoverer': {
                'name': 'static',
                'static': {
                    'adjacency': {
                        '1': ['2'],
                        '2': ['1'],
                    },
                },
            },
            'communicator': {
                'name': 'sockets',
                'sockets': {
                    'nodes_and_endpoints': [
                        ('1', (LOOPBACK, MY_ID_SERVER_MY_PORT)),
                        ('2', (LOOPBACK, MY_ID_SERVER_NEIGHBOR_PORT)),
                    ],
                },
            },
            'my_id': 0,
            'split': {
                'num_nodes': 2,
                'seed': 1234,
            },
            'pipelines': {
                'just': ['Auton_Logistic_regression'],
            }
        },
        'problem_type': {
            'task': 'binary_classification',
        }
    })

    dut = DistributedWrangler(problem_definition=pdef, my_id=1)

    train_msg = {
        'target': {'target': train_df['target'].tolist()},
        'covariates': train_df.drop(columns=['target']).to_dict(orient='list'),
    }

    neighbor = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
    neighbor.bind((LOOPBACK, MY_ID_SERVER_NEIGHBOR_PORT))
    neighbor.setblocking(False)
    server = None
    exception = None
    try:
        server = Process(target=dut.server(host=LOOPBACK, port=MY_ID_SERVER_WEB_PORT))
        server.start()

        time.sleep(2.0)

        r = requests.post(f'http://localhost:{MY_ID_SERVER_WEB_PORT}/wrangler/v1.0/fit',
                          json={
                              'data': train_msg,
                          },
                          timeout=None)

        assert r.text == '{"status":"OK"}\n'

        ready = select.select([neighbor], [], [], 60.0)
        if ready[0]:
            _, response_addr = neighbor.recvfrom(1024)
        else:
            raise TimeoutError('Timeout waiting for neighbor to respond')

        assert response_addr == (LOOPBACK, MY_ID_SERVER_MY_PORT)

    except Exception as e:  # pylint: disable=broad-except
        exception = e
        logging.debug("exception %s in test_server_sunny_day", e)
    finally:
        if server is not None:
            server.terminate()
            server.join()

    if exception is not None:
        raise exception
