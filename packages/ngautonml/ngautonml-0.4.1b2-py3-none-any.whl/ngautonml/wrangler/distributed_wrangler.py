'''This file handles integration for all the steps in distributed algorithms.'''
import logging
from queue import Queue
from typing import Callable, Dict, Optional, Type

from flask import Flask, request

from ngautonml.neighbor_manager.node_id import NodeID


from ..config_components.distributed_config import DistributedConfig
from ..generator.designator import Designator
from ..instantiator.executable_pipeline import ExecutablePipeline
from ..searcher.params import Override, Overrides, ParamRange, ParamRanges, Selector
from ..searcher.searcher import Searcher, SearcherImpl
from ..splitters.impl.splitter import Splitter
from ..templates.impl.pipeline_template import PipelineTemplate
from ..wrangler.dataset import RoleName
from ..wrangler.exception_thread import ExceptionThread

from .constants import Matcher, RangeMethod
from .wrangler_base import WranglerBase
from .wrangler_result import WranglerResult
from .logger import Logger

logger = Logger(__file__, logging.INFO, to_stdout=True).logger()


class DistributedWrangler(WranglerBase):
    '''The wrangler is the central control object for distributed algorithms.'''
    _results: Queue[WranglerResult]
    _stop: bool = False
    _splitter: Splitter
    _fitter_thread: Optional[ExceptionThread] = None

    def __init__(self, *args,
                 searcher: Optional[Type[Searcher]] = None,
                 my_id: Optional[int] = None,
                 **kwargs):
        self._results = Queue()
        super().__init__(*args, **kwargs)

        # Inject the DistributedConfig as a hyperparam called 'distributed'
        #   for all distributed algorithms.
        distributed_overrides = Overrides()
        config = self._pd.get_conf('distributed')
        assert isinstance(config, DistributedConfig)
        if my_id is not None:
            config.my_id = NodeID(my_id)

        distributed_overrides.append(
            Override(
                selector=Selector({
                    Matcher.TAGS: {'distributed': 'true'}
                }),
                params=ParamRanges(distributed=ParamRange(
                    method=RangeMethod.FIXED,
                    prange=config
                )),
                no_show=True
            )
        )

        self._searcher = (searcher or SearcherImpl)(
            hyperparams=self._pd.hyperparams,
            inject=distributed_overrides)

        self._bound_pipelines = self._build_pipelines()
        executable_pipelines: Dict[Designator, ExecutablePipeline] = {
            pipeline.designator: self._instantiator_factory.instantiate(
                kind=self._executor.kind, pipeline=pipeline
            )
            for pipeline in self._bound_pipelines.values()
        }
        self._all_executable_pipelines = executable_pipelines
        self._current_executable_pipelines = executable_pipelines
        # We must init the data loader before we start the fitter thread.
        # The MemoryDataLoader can not search the stack for variables from a thread.
        self._find_data_loader()

    def _fit_loop(self, stop: Callable[[], bool]):
        '''This function is the data thread to process data.'''
        distributed = self._pd.get_conf('distributed')
        assert isinstance(distributed, DistributedConfig)
        while not stop():
            next_data = self._find_data_loader().poll(timeout=distributed.polling_interval)
            self.fit(next_data)  # sets self._current_trained_pipelines

    def lookup_templates(self) -> Dict[str, PipelineTemplate]:
        '''Look up the templates that match the problem definition.

        {
            'distributed': {
                'pipelines': {
                    'just': ['autonLogisticRegression', 'some other algorithm']
                    'memory': ['my_memory_pipeline']
                    'templated': [
                        {
                            'template': 'binary_tabular_classification',
                            'alg': 'AutonLogisticRegression'
                        },
                        {
                            'data_type': 'tabular',
                            'task': 'binary_classification',
                            'alg': 'some_other_alg'
                        }
                    ]
                }
            }
        }
        '''
        distributed = self._pd.get_conf('distributed')
        assert isinstance(distributed, DistributedConfig)

        retval: Dict[str, PipelineTemplate] = {}

        for loader_name, arguments in distributed.pipelines.items():
            pipeline_loader = self._pipeline_loader_catalog.lookup_by_name(loader_name)
            for argument in arguments:
                if isinstance(argument, str):
                    argument = [argument]
                args = []
                kwargs = {}
                if isinstance(argument, list):
                    args = argument
                if isinstance(argument, dict):
                    kwargs = argument
                loaded_pipeline = pipeline_loader.load(*args, **kwargs)
                retval[loaded_pipeline.designator] = loaded_pipeline

        return retval

    def results(self) -> Queue[WranglerResult]:
        '''Return the results queue.'''
        return self._results

    def start(self) -> None:
        '''Start the wrangler threads.'''

        logger.debug('DistributedWrangler starting wrangler threads: %x', id(self))
        self._stop = False
        assert self._all_executable_pipelines is not None
        for executable_pipeline in self._all_executable_pipelines.values():
            logger.debug('DistributedWrangler starting pipeline: %s(%x)',
                         executable_pipeline, id(executable_pipeline))
            executable_pipeline.start()
        if self._fitter_thread is None:
            self._fitter_thread = ExceptionThread(target=self._fit_loop, kwargs={
                'stop': lambda: self._stop
            })
        self._fitter_thread.start()

    def stop(self) -> None:
        '''Stop the wrangler threads.'''
        logger.debug('DistributedWrangler stopping wrangler threads: %x', id(self))
        self._stop = True
        if self._fitter_thread is not None:
            self._fitter_thread.join()
            self._fitter_thread = None
        assert self._all_executable_pipelines is not None
        for executable_pipeline in self._all_executable_pipelines.values():
            logger.debug('DistributedWrangler stopping pipeline: %s(%x)',
                         executable_pipeline, id(executable_pipeline))
            executable_pipeline.stop()

    def build_dataset_from_json(self, json_data: Dict) -> Dict:
        '''Build a dataset from JSON data.'''
        return self._find_data_loader().build_dataset_from_json(json_data)

    def server(self, host='127.0.0.1', port=8080) -> Callable[[], None]:
        '''Start the REST node server.'''
        app = Flask(__name__)

        @app.get('/wrangler/v1.0/status')
        def status():
            trained = all(pipeline.trained
                          for pipeline in self._current_executable_pipelines.values())
            return {'status': 'OK' if trained else 'UNTRAINED'}

        @app.route('/wrangler/v1.0/fit', methods=['GET', 'POST'])
        def fit():
            if request.method == 'GET':
                return status()
            if request.method == 'POST':
                try:
                    dataset = self.build_dataset_from_json(request.json)
                    self.fit(dataset=dataset)
                except BaseException as e:  # pylint: disable=broad-except
                    return {'error': str(e)}
                return status()
            raise ValueError(f'Invalid request method {request.method}')

        @app.route('/wrangler/v1.0/predict', methods=['GET', 'POST'])
        def predict():
            if request.method == 'GET':
                return status()
            if request.method == 'POST':
                dataset = self.build_dataset_from_json(request.json)
                result = self.predict(new_data=dataset)
                retval = {}
                for key, value in result.items():
                    target_col = value.prediction.metadata.roles[RoleName.TARGET][0].name
                    retval[key] = value.prediction.predictions[target_col].tolist()
                return retval
            raise ValueError(f'Invalid request method {request.method}')

        def retval():
            self.start()
            logger.info('DistributedWrangler starting server on %s:%s', host, port)
            app.run(host=host, port=port)

        return retval
