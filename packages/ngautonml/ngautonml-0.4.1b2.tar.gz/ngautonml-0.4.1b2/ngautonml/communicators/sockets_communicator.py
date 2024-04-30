'''Sends and recieves messages using UDP sockets.'''

# Copyright (c) 2024 Carnegie Mellon University
# This code is subject to the license terms contained in the LICENSE file.

import logging
from queue import Queue
import socket
from typing import Callable, Dict, List, Optional, Set


from ..config_components.distributed_config import DistributedConfig
from ..neighbor_manager.event import NewNeighbor, Recv
from ..neighbor_manager.node_id import NodeID
from ..wrangler.constants import Defaults
from ..wrangler.exception_thread import ExceptionThread
from ..wrangler.logger import Logger

from .impl.ip_endpoint import IPEndpoint
from .impl.communicator import Communicator
from .impl.communicator_catalog import CommunicatorCatalog

logger = Logger(__file__, logging.DEBUG).logger()


def _socket_listener(queue: Queue,
                     sock: socket.socket,
                     assign_node_id: Callable[[IPEndpoint], NodeID],
                     stop: Callable[[], bool],
                     timeout: int,
                     known_neighbors: Set[NodeID]):

    while True:
        try:
            if stop():
                return
            payload, addr = sock.recvfrom(1024)
            endpoint = IPEndpoint(host=addr[0], port=addr[1])
            neighbor = assign_node_id(endpoint)
            if neighbor not in known_neighbors:
                known_neighbors.add(neighbor)
                queue.put(NewNeighbor(neighbor=neighbor), timeout=timeout)
            queue.put(Recv(neighbor, payload), timeout=timeout)
        except socket.timeout:
            pass


class SocketsCommunicator(Communicator):
    '''Sends and recieves messages using UDP sockets.'''
    name: str = 'sockets'
    tags: Dict[str, List[str]] = {}
    _stop: bool
    _node_to_endpoint: Dict[NodeID, IPEndpoint]
    _endpoint_to_node: Dict[IPEndpoint, NodeID]
    _sock: Optional[socket.socket]
    _next_node_id: NodeID
    _listener: Optional[ExceptionThread] = None

    def __init__(self,
                 known_neighbors: Set[NodeID],
                 my_id: NodeID,
                 distributed: DistributedConfig):
        self._node_to_endpoint = {}
        self._endpoint_to_node = {}
        self._stop = False
        self._sock = None
        self._next_node_id = NodeID(1)
        for (node, endpoint) in distributed.nodes_and_endpoints:
            assert isinstance(endpoint, IPEndpoint), (
                f'BUG: endpoint={endpoint} is if type={type(endpoint)}, not IPEndpoint'
            )
            self._node_to_endpoint[node] = endpoint
            self._endpoint_to_node[endpoint] = node
            if node >= self._next_node_id:
                self._next_node_id = NodeID(node + 1)
        super().__init__(my_id=my_id, known_neighbors=known_neighbors, distributed=distributed)

    def stop(self):
        '''Tell threads to terminate themselves.'''
        if self._listener is not None:
            logger.debug('Stopping SocketsCommunicator: %s', self._listener)
            self._stop = True
            self._listener.join()
            self._listener = None

    def assign_node_id(self, endpoint: IPEndpoint) -> NodeID:
        '''Assign a node ID to the given endpoint (or find one that was already assigned).'''
        if endpoint not in self._endpoint_to_node:
            node = self._next_node_id
            self._next_node_id = NodeID(self._next_node_id + 1)
            self._endpoint_to_node[endpoint] = node
            self._node_to_endpoint[node] = endpoint
        return self._endpoint_to_node[endpoint]

    def lookup_endpoint(self, node: NodeID) -> IPEndpoint:
        '''Find the IPEndpoint that corresponds to the node.'''
        return self._node_to_endpoint[node]

    def start(self,
              queue: Queue,
              timeout: float = Defaults.LISTENER_TIMEOUT) -> None:
        self._sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self._sock.settimeout(timeout)
        my_endpoint = self._node_to_endpoint[self._my_id]
        self._sock.bind((my_endpoint.host, my_endpoint.port))
        self._stop = False
        self._listener = ExceptionThread(target=_socket_listener, kwargs={
            'queue': queue,
            'sock': self._sock,
            'assign_node_id': self.assign_node_id,
            'stop': lambda: self._stop,
            'timeout': timeout,
            'known_neighbors': self._known_neighbors,
        })
        self._listener.start()

    def send(self,
             dest_id: NodeID,
             payload: bytes) -> int:
        '''Send a message to the node with dest_id.

        Return value is the size of the message sent.
        '''
        assert self._sock is not None, (
            'BUG: send() called before start().'
        )
        dest_endpoint = self._node_to_endpoint[dest_id]
        return self._sock.sendto(payload, dest_endpoint.as_tuple)

    def send_all(self, payload: bytes) -> int:
        '''Send a message to all known neighbors.

        Return value is a count of neighbors we sent to.
        '''
        sent_count = 0
        for node in list(self._known_neighbors):
            self.send(dest_id=node, payload=payload)
            sent_count += 1
        return sent_count


def register(catalog: CommunicatorCatalog) -> None:
    '''Register all objects in this file.'''
    catalog.register(SocketsCommunicator)
