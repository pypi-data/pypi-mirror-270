'''Base class for distributed alogorithm instances.'''

import abc
from copy import deepcopy
import threading
import time
from typing import Any, Callable, Dict, Generic, Iterable, Optional, Set, TypeVar

from ...algorithms.impl.fittable_algorithm_instance import UntrainedError
from ...config_components.distributed_config import DistributedConfig
from ...neighbor_manager.event import Recv
from ...neighbor_manager.node_id import NodeID
from ...neighbor_manager.neighbor_manager import NeighborManager
from ...neighbor_manager.neighbor_manager_impl import NeighborManagerImpl
from ...wrangler.dataset import Dataset
from ...wrangler.exception_thread import ExceptionThread
from ...wrangler.logger import Logger

from ..impl.algorithm import Algorithm, HyperparamError
from ..impl.fittable_algorithm_instance import FittableAlgorithmInstance


logger = Logger(__file__, to_stdout=False).logger()


NeighborStateSubclass = TypeVar('NeighborStateSubclass', bound='NeighborState')


class NoDataError(Exception):
    '''No data was provided to the algorithm.'''


class NeighborState(abc.ABC, Generic[NeighborStateSubclass]):
    '''A message from a neighbor in the distributed network.'''

    @abc.abstractmethod
    def encode(self) -> bytes:
        '''Encode a message for distributed neighbors. '''

    @classmethod
    @abc.abstractmethod
    def decode(cls, serialized_model: bytes) -> NeighborStateSubclass:
        '''Decode a message from distributed neighbors.

        This should just redirect to the relevant NeighborState subclass.
        '''

    @abc.abstractmethod
    def should_send(self,
                    distributed: DistributedConfig,
                    last_state_sent: Optional[Any]) -> bool:
        '''Decide whether to send a message to neighbors.

        last_state_sent is an instance of type(self) or None.
        '''


class DistributedAlgorithmInstance(FittableAlgorithmInstance):
    '''Base class for distributed ajsons.'''

    _known_neighbors: Set[NodeID]
    _my_id: NodeID

    _lock_model: Optional[threading.Lock] = None
    _neighbor_manager: Optional[NeighborManager] = None
    _fit_thread: Optional[ExceptionThread] = None
    _read_thread: Optional[ExceptionThread] = None
    _neighbor_models: Dict[NodeID, NeighborState]
    _distributed: DistributedConfig

    _last_dataset: Optional[Dataset] = None
    _last_state_sent: Optional[NeighborState] = None
    _my_state: Optional[NeighborState] = None
    _pending_message_from_neighbor: bool = False
    _stop: bool = False

    def __deepcopy__(self, memo: Dict[int, object]) -> 'DistributedAlgorithmInstance':
        '''Deepcopy implementation.'''
        # We don't want to deepcopy the lock, threads, the neighbor manager, the
        # last dataset, pending message state, or the stop flag.
        alg_name = self._algorithm.name if self._algorithm is not None else 'unknown'
        logger.debug('%s: deepcopying: %x', alg_name, id(self))
        assert self._algorithm is not None
        retval = type(self)(parent=self._algorithm,
                            distributed=self._distributed)
        retval._known_neighbors = deepcopy(self._known_neighbors, memo=memo)
        retval._my_id = self._my_id
        retval._neighbor_models = deepcopy(self._neighbor_models, memo=memo)
        retval._distributed = deepcopy(self._distributed, memo=memo)
        retval._last_dataset = None
        retval._last_state_sent = deepcopy(self._last_state_sent, memo=memo)
        retval._my_state = deepcopy(self._my_state, memo=memo)
        retval._pending_message_from_neighbor = False
        retval._trained = self._trained
        retval._lock_model = None
        return retval

    def __init__(self,
                 parent: Algorithm,
                 distributed: DistributedConfig,
                 **kwargs):
        super().__init__(parent, **kwargs)
        # TODO(piggy/merrittk): This should become a BUG once the searcher
        # does this check.
        if kwargs:
            raise HyperparamError(f'Unexpected hyperparams to AutonLR: {kwargs}')
        self._distributed = distributed
        self._my_id = distributed.my_id
        self._neighbor_models = {}
        self._known_neighbors = set()
        self._lock_model = threading.Lock()

    @property
    def _neighbor_models_iter(self) -> Iterable[NeighborState]:
        for _, v in self._neighbor_models.items():
            assert isinstance(v, NeighborState), (
                'BUG: expected neighbor_models to contain NeighborState, '
                f'instead found {v} of type {type(v)}'
            )
            yield v

    def start(self) -> None:
        '''Start all supporting threads.'''
        alg_name = self._algorithm.name if self._algorithm is not None else 'unknown'
        logger.debug('%s: %s is starting: %x', alg_name, self._my_id, id(self))
        self._stop = False
        if self._neighbor_manager is None:
            self._neighbor_manager = self._init_neighbor_manager()
            self._neighbor_manager.start()
        self._fit_thread = ExceptionThread(target=self._fit_periodically, kwargs={
            'stop': lambda: self._stop
        })
        self._fit_thread.start()
        self._read_thread = ExceptionThread(target=self._read_from_neighbors, kwargs={
            'stop': lambda: self._stop
        })
        self._read_thread.start()

    def stop(self) -> None:
        '''Stop all supporting threads.'''
        alg_name = self._algorithm.name if self._algorithm is not None else 'unknown'
        logger.debug('%s: %s is stopping: %x', alg_name, self._my_id, id(self))
        self._stop = True
        if self._fit_thread is not None:
            self._fit_thread.join()
        if self._read_thread is not None:
            self._read_thread.join()
        if self._neighbor_manager is not None:
            self._neighbor_manager.stop()

    def _init_neighbor_manager(self) -> NeighborManager:
        comm = self.algorithm.communicator_catalog.lookup_by_name(
            self._distributed.communicator)
        disc = self.algorithm.discoverer_catalog.lookup_by_name(
            self._distributed.discoverer)
        communicator = comm(distributed=self._distributed,
                            known_neighbors=self._known_neighbors,
                            my_id=self._my_id)
        discoverer = disc(config=self._distributed, communicator=communicator)
        retval = NeighborManagerImpl(discoverer=discoverer)
        return retval

    def _read_from_neighbors(self, stop: Callable[[], bool]) -> None:
        '''Read from neighbors and update the neighbor states.'''
        logger.debug('%s is starting to receive from neighbors: %x', self._my_id, id(self))
        while not stop():
            if self._neighbor_manager is not None:
                for event in self._neighbor_manager.poll_for_events(
                    timeout=self._distributed.polling_interval
                ):
                    logger.debug('%s is reading %s', self._my_id, event)
                    if isinstance(event, Recv):
                        self._recv(event.neighbor, event.payload)
            else:
                time.sleep(self._distributed.polling_interval)

    def _fit_periodically(self, stop: Callable[[], bool]):
        '''Refit if we have seen a message from a neighbor and enough time passed.'''
        logger.debug('%s is starting to fit periodically: %x', self._my_id, id(self))
        while not stop():
            if self._pending_message_from_neighbor:
                logger.debug('%s is spontaneously fitting', self._my_id)
                self._fit_data_optional(self._last_dataset)
            time.sleep(self._distributed.polling_interval)

    def _recv(self, neighbor_id: NodeID, serialized_model: bytes) -> None:
        '''Receive a message from a neighbor.'''
        model = self._decode(serialized_model)
        assert self._lock_model is not None
        with self._lock_model:
            logger.debug('%s received from %s', self._my_id, neighbor_id)
            self._pending_message_from_neighbor = True
            self._neighbor_models[neighbor_id] = model

    @abc.abstractmethod
    def _decode(self, serialized_model: bytes) -> NeighborState:
        '''Decode a message from distributed neighbors. '''

    def _send(self) -> None:
        '''Send the model to all neighbors.

        Must be called with the model lock held.
        '''
        logger.debug('%s is sending', self._my_id)
        assert self._my_state is not None, (
            'BUG: self._my_state should not be None when _send is called.'
        )
        if self._neighbor_manager is not None:
            self._neighbor_manager.send_all(self._my_state.encode())
        # Only reset the last_state_sent if we actually sent a message.
        # We want to catch cumulative drift in self._my_state.v.
        self._last_state_sent = deepcopy(self._my_state)

    def _fit_data_optional(self, dataset: Optional[Dataset], **kwargs) -> None:
        '''Fit the model to the data. This version does not require a dataset.'''
        assert self._lock_model is not None
        with self._lock_model:
            if dataset is not None:
                self._last_dataset = dataset
            self._fit(dataset, **kwargs)

            self._trained = True
            self._pending_message_from_neighbor = False
            if (self._my_state is not None
                and self._my_state.should_send(
                    distributed=self._distributed,
                    last_state_sent=self._last_state_sent)):
                logger.debug('%s is about to send (in fit)', self._my_id)
                self._send()

    def fit(self, dataset: Optional[Dataset], **kwargs) -> None:
        '''Fit the model to the data.

        If dataset is None, we process information from neighbors.
        If dataset is not None but is empty, we ignore it. This allows
        us to work with special data loaders.
        '''
        self._fit_data_optional(dataset=dataset, **kwargs)

    @abc.abstractmethod
    def _fit(self, dataset: Optional[Dataset], **kwargs):
        '''Fit the model to the data. This is the actual implementation of fit.'''

    def predict(self, dataset: Optional[Dataset], **kwargs) -> Optional[Dataset]:
        '''Apply model to input dataset to create output.

        This handles lock acquisition and generalized distributed work.
        '''
        if not self.trained:
            raise UntrainedError(
                f'Algorithm "{self.catalog_name}" needs to be fit before it can predict')

        if dataset is None:
            logger.debug('%s predict got None dataset', self._my_id)
            return None

        assert self._lock_model is not None
        with self._lock_model:

            retval = self._predict(dataset=dataset, **kwargs)

        return retval

    @abc.abstractmethod
    def _predict(self, dataset: Optional[Dataset], **kwargs) -> Optional[Dataset]:
        '''Apply model to input dataset to create output.

        This handles model-speific work and does not handle general tasks.q
        '''
