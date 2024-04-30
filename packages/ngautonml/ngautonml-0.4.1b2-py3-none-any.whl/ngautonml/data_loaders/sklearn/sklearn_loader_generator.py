'''Generates a constructor for an SklearnLoader.'''
# Copyright (c) 2024 Carnegie Mellon University
# This code is subject to the license terms contained in the LICENSE file.

# pylint: disable=duplicate-code,too-many-arguments
from copy import deepcopy
from typing import Any, Callable, Dict, List, Optional, Type
import importlib
import random

from numpy.random import RandomState
import pandas as pd

from ...wrangler.constants import Defaults
from ...wrangler.dataset import Dataset
from ..impl.data_loader_catalog import DataLoaderCatalog
from ..impl.dataframe_loader import DataframeLoader
from .sklearn_loader_interface import SklearnLoaderInterface


def _load_train_impl(self: SklearnLoaderInterface) -> Dataset:
    '''Implementation for _load_train() in the SklearnLoader we generate'''
    # pylint: disable=protected-access
    params = deepcopy(self._config.params)
    if self.tags.get('supports_random_seed', ['false'])[0] == 'true':
        if 'random_seed' in params:
            params['random_state'] = RandomState(params.pop('random_seed'))
        elif params.get('random_state', None) is None:
            params['random_state'] = RandomState(Defaults.SEED)

    if self.tags.get('uses_return_X_y', ['false'])[0] == 'true':
        params['return_X_y'] = True

    if self.tags.get('uses_as_frame', ['false'])[0] == 'true':
        params['as_frame'] = True

    (x, y) = self._impl._loader(**params)

    retval_df = pd.DataFrame(x)
    retval_df['y'] = y

    # Make sure all column names are strings
    #   (casting to Index to make mypy happy)
    retval_df.columns = pd.core.indexes.base.Index([str(n) for n in retval_df.columns])
    retval = self._dataset(data=retval_df)
    return retval


def _load_test_impl(self: SklearnLoaderInterface) -> Optional[Dataset]:
    '''Implementation for _load_test() in the SklearnLoader we generate'''
    _ = self
    retval = None  # makes pylint happy...
    return retval


class SklearnLoaderGenerator():
    '''Generates a constructor for an SklearnLoader.'''
    _loader: Callable[..., Any]

    def __init__(self,
                 name: str,
                 loader: Optional[type] = None,
                 tags: Optional[Dict[str, List[str]]] = None,
                 **hyperparams: Any):
        self.name = name
        if loader is None:
            loader = self._load_module(name)
        self._loader = loader
        if tags is not None:
            self.tags = tags.copy()
        else:
            self.tags = {}
        super().__init__(**hyperparams)

    def _random_name(self) -> str:
        # We don't actually care about collisions as we never look
        # these constructors up by name.
        return f'GeneratedSklearnLoader{random.randint(0, 999999999)}'

    def _load_module(self, name: str):
        # Split name into module part (e.g. sklearn.linear_model)
        # and constructor part (e.g. LinearRegression)
        parts = name.split('.')
        constructor_part = parts[-1]
        module = importlib.import_module('.'.join(parts[:-1]))
        # Load the constructor.
        return getattr(module, constructor_part)

    def new_class(self) -> Type[DataframeLoader]:
        '''Generate a constructor for an SklearnLoader.'''
        return type(self._random_name(), (DataframeLoader, ), {
            "name": self.name,
            "tags": self.tags.copy(),
            "_load_train": _load_train_impl,
            "_load_test": _load_test_impl,
            "_impl": self,
        })


def register(catalog: DataLoaderCatalog):  # pylint: disable=unused-argument
    '''Nothing to register.

    All subclasses of SklearnAlgorithm are registered in sklearn_algorithms.py
    '''
