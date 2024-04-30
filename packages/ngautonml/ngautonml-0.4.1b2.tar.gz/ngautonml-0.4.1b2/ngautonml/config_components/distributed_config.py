'''Specifies  a distributed AI setting.'''

# Copyright (c) 2024 Carnegie Mellon University
# This code is subject to the license terms contained in the LICENSE file.

from enum import Enum
from typing import Any, Dict, List, Optional, Set, Tuple

from ..communicators.impl.endpoint import Endpoint
from ..communicators.impl.ip_endpoint import IPEndpoint
from ..neighbor_manager.node_id import NodeID
from ..wrangler.constants import Defaults

from .impl.config_component import (
    ConfigComponent, ConfigError, InvalidValueError, ValidationErrors)
from .impl.config_component_catalog import ConfigComponentCatalog


class SplitConfig(ConfigComponent):
    '''Specifies how to split data for simulations.'''

    @property
    def seed(self) -> int:
        '''Seed for random number generation.'''
        return self._get_with_default('seed', dflt=Defaults.SEED)

    @property
    def num_nodes(self) -> int:
        '''The number of nodes in the system.'''
        return self._get('num_nodes')


class DistributedConfig(ConfigComponent):
    '''Specifies distributed configration in a distributed AI setting.'''
    name = 'distributed'
    tags: Dict[str, Any] = {}

    class Constants(Enum):
        '''Keys below the top level.'''
        NAME = 'name'
        # Discoverers
        STATIC = 'static'  # Static neighbor configuration
        ADJACENCY = 'adjacency'
        EDGES = 'edges'

        DYNAMIC = 'dynamic'  # Simple dynamic neighbor configuration
        # Communicators
        SOCKETS = 'sockets'
        NODES_AND_ENDPOINTS = 'nodes_and_endpoints'

    class Defaults(Enum):
        '''Default values'''
        DISCOVERER = 'dynamic'
        COMMUNICATOR = 'sockets'
        POLLING_INTERVAL = '0.1'
        FIT_EPS = '0.0'

    class Keys(Enum):
        '''Valid keys for the top level.'''
        COMMUNICATOR = 'communicator'  # Name of the communicator to use
        DISCOVERER = 'discoverer'  # Name of the discoverer to use
        FIT_EPS = 'fit_eps'  # Minimum change in model before sending to neighbors
        MY_ID = 'my_id'  # ID of the current node
        PIPELINES = 'pipelines'  # Clause of pipeline loaders
        POLLING_INTERVAL = 'polling_interval'  # Time for models to wait between refitting
        SPLIT = 'split'  # Info about splitting of the data for simulations

    def required_keys(self) -> Set[str]:
        return {
            self.Keys.DISCOVERER.value,
            self.Keys.COMMUNICATOR.value
        }

    def get_static_adjacency(self, my_id: NodeID) -> Optional[List[NodeID]]:
        '''If we have a static config, get the list of my_id's neighbors.

        Returns None if there is no static config.
        '''
        if not self._exists(self.Keys.DISCOVERER, self.Constants.STATIC):
            return None
        if self._get(self.Keys.DISCOVERER, self.Constants.NAME) != self.Constants.STATIC.value:
            return None
        if self._exists(self.Keys.DISCOVERER, self.Constants.STATIC, self.Constants.ADJACENCY):
            my_neighbors: List[int] = self._get(
                self.Keys.DISCOVERER, self.Constants.STATIC, self.Constants.ADJACENCY, str(my_id))
            return [NodeID(n) for n in sorted(my_neighbors)]
        if self._exists(self.Keys.DISCOVERER, self.Constants.STATIC, self.Constants.EDGES):
            retval = set()
            for edge in self._get(
                self.Keys.DISCOVERER, self.Constants.STATIC, self.Constants.EDGES
            ):
                if edge[0] == int(my_id):
                    retval.add(edge[1])
                if edge[1] == int(my_id):
                    retval.add(edge[0])
            return [NodeID(n) for n in sorted(retval)]
        raise NotImplementedError(
            f'unrecognized static clause(s): '
            f'{self._get(self.Keys.DISCOVERER, self.Constants.STATIC).keys()}')

    @property
    def nodes_and_endpoints(self) -> List[Tuple[NodeID, Endpoint]]:
        '''Get a preconfigured relationship between nodes and endpoints.'''
        retval: List[Tuple[NodeID, Endpoint]] = []
        if not self._exists(
            self.Keys.COMMUNICATOR, self.Constants.SOCKETS, self.Constants.NODES_AND_ENDPOINTS
        ):
            return retval
        for node, endpoint in self._get(
            self.Keys.COMMUNICATOR, self.Constants.SOCKETS, self.Constants.NODES_AND_ENDPOINTS
        ):
            node_id = NodeID(int(node))
            # We only know how to build IP endpoints at the moment.
            ip, port = endpoint
            retval.append(
                (node_id, IPEndpoint(ip, int(port)))
            )
        return retval

    def validate(self, **kwargs: Any) -> None:
        errors: List[ConfigError] = []

        if self._exists(self.Keys.DISCOVERER, self.Constants.STATIC, self.Constants.EDGES):
            edges = self._get(
                self.Keys.DISCOVERER, self.Constants.STATIC, self.Constants.EDGES)
            if not isinstance(edges, list):
                raise ValidationErrors([InvalidValueError(
                    f'edges must be a list, instead found {edges} of type {type(edges)}')])
            for edge in self._get(
                self.Keys.DISCOVERER, self.Constants.STATIC, self.Constants.EDGES
            ):
                if len(edge) != 2:
                    errors.append(InvalidValueError(
                        f'Edge {edge} does not have exactly two elements.'))

        if len(errors) > 0:
            raise ValidationErrors(errors=errors)

    @property
    def fit_eps(self) -> float:
        '''Minimum change in model before sending to neighbors.'''
        return float(self._get_with_default(
            self.Keys.FIT_EPS, dflt=self.Defaults.FIT_EPS.value))

    @property
    def polling_interval(self) -> float:
        '''Time for models to wait between refitting.'''
        return float(self._get_with_default(
            self.Keys.POLLING_INTERVAL, dflt=self.Defaults.POLLING_INTERVAL.value))

    @property
    def discoverer(self) -> str:
        '''Which discoverer should we use?

        Options include 'static' and 'dynamic'.
        '''
        return self._get_with_default(
            self.Keys.DISCOVERER, self.Constants.NAME, dflt=self.Defaults.DISCOVERER.value)

    @property
    def communicator(self) -> str:
        '''Which communicator should we use?

        Options include 'sockets'.
        '''
        return self._get_with_default(
            self.Keys.COMMUNICATOR, self.Constants.NAME, dflt=self.Defaults.COMMUNICATOR.value)

    @property
    def split(self) -> Optional[SplitConfig]:
        '''Info about splitting of the data for simulations.'''
        clause = self._get_with_default(self.Keys.SPLIT, dflt=None)
        if clause is None:
            return None
        assert isinstance(clause, dict), (
            f'BUG: expected a dict at {self.Keys.SPLIT}, instead found {type(clause)}'
        )

        return SplitConfig(clause)

    @property
    def my_id(self) -> NodeID:
        '''Node ID for the current node.'''
        # TODO(Piggy): rewrite this, injecting my_id from the command line.
        return self._get_with_default(self.Keys.MY_ID, dflt=NodeID(1))

    @my_id.setter
    def my_id(self, value: NodeID) -> None:
        '''Set the node ID for the current node.'''
        self._clause[self.Keys.MY_ID.value] = value

    @property
    def pipelines(self) -> Dict[str, List[Any]]:
        '''List of pipeline loaders to use.'''
        return self._get_with_default(self.Keys.PIPELINES, dflt={})


def register(catalog: ConfigComponentCatalog) -> None:
    '''Register all the objects in this file.'''
    catalog.register(DistributedConfig)
