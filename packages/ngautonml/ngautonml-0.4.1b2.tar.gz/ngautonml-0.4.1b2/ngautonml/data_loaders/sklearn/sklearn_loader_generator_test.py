'''Tests for sklearn_loader.py and sklearn_laoders.py'''
from copy import deepcopy

import pandas as pd

from ...config_components.dataset_config import DatasetConfig
from ..impl.data_loader_auto import DataLoaderCatalogAuto
from ..impl.dataframe_loader import DataframeLoader
from .sklearn_loader_generator import SklearnLoaderGenerator

# pylint: disable=missing-function-docstring, duplicate-code


MOONY_CLAUSE = {
    'input_format': 'sklearn.datasets.make_moons',
    'params': {
        'n_samples': 5,
        'shuffle': True,
        'noise': None
    }
}


def test_moony_day() -> None:
    dut = SklearnLoaderGenerator(
        name='sklearn.datasets.make_moons',
        tags={
            'input_format': ['sklearn.datasets.make_moons'],
            'loaded_format': ['pandas_dataframe'],
            'supports_random_seed': ['true']
        }
    )

    got = dut.new_class()

    config = DatasetConfig(clause=MOONY_CLAUSE)

    inst = got(config=config)

    assert isinstance(inst, DataframeLoader)

    got_data = inst.load_train()
    want_df = pd.DataFrame({
        '0': [-1.0, 1, 1, 0, 2],
        '1': [0.0, 0, -0.5, 0.5, 0.5],
        'y': [0, 0, 1, 1, 1]
    })
    assert got_data is not None
    pd.testing.assert_frame_equal(got_data.dataframe, want_df)


def test_set_seed() -> None:
    dut = SklearnLoaderGenerator(
        name='sklearn.datasets.make_moons',
        tags={
            'input_format': ['sklearn.datasets.make_moons'],
            'loaded_format': ['pandas_dataframe'],
            'supports_random_seed': ['true']
        }
    )

    got = dut.new_class()

    clause = deepcopy(MOONY_CLAUSE)
    assert isinstance(clause['params'], dict)
    clause['params']['random_seed'] = 1337
    config = DatasetConfig(clause=clause)

    inst = got(config=config)
    assert isinstance(inst, DataframeLoader)

    got_data = inst.load_train()
    want_df = pd.DataFrame({
        '0': [1.0, 0, -1, 1, 2],
        '1': [-0.5, 0.5, 0, 0, 0.5],
        'y': [1, 1, 0, 0, 1]
    })
    assert got_data is not None
    pd.testing.assert_frame_equal(got_data.dataframe, want_df)


def test_lookup() -> None:
    config = DatasetConfig(clause=MOONY_CLAUSE)
    dut = DataLoaderCatalogAuto().construct_instance(config=config)

    got_data = dut.load_train()
    want_df = pd.DataFrame({
        '0': [-1.0, 1, 1, 0, 2],
        '1': [0.0, 0, -0.5, 0.5, 0.5],
        'y': [0, 0, 1, 1, 1]
    })
    assert got_data is not None
    pd.testing.assert_frame_equal(got_data.dataframe, want_df)
    assert dut.__class__.__name__.startswith('GeneratedSklearnLoader')


DIABETES_CLAUSE = {
    'input_format': 'sklearn.datasets.load_diabetes',
    'params': {
        'scaled': True
    }
}


def test_diabetes() -> None:
    dut = SklearnLoaderGenerator(
        name='sklearn.datasets.load_diabetes',
        tags={
            'input_format': ['sklearn.datasets.load_diabetes'],
            'loaded_format': ['pandas_dataframe'],
            'supports_random_seed': ['false'],
            'uses_return_X_y': ['true'],
            'uses_as_frame': ['true']
        }
    )
    got = dut.new_class()

    clause = deepcopy(DIABETES_CLAUSE)
    config = DatasetConfig(clause=clause)

    inst = got(config=config)
    assert isinstance(inst, DataframeLoader)

    got_data = inst.load_train()
    assert got_data is not None
    assert got_data.dataframe.shape == (442, 11)
    assert list(got_data.dataframe.columns) == [
        'age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6', 'y'
    ]
