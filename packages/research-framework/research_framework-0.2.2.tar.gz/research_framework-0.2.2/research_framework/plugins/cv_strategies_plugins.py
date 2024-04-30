import traceback
from sklearn.model_selection import ShuffleSplit
from enum import Enum
import randomname
import wandb
import wandb.sdk
import numpy as np

from research_framework.base.plugin.base_wrapper import BaseWrapper
from research_framework.container.container import Container
from research_framework.dataset.standard_dataset import StandardDataset
from research_framework.pipeline.model.pipeline_model import FilterModel, InputFilterModel, SimplePipelineModel, WandbRunPipelineModel


class UnsupervisedRun:
    def __init__(self, data, scorer, metrics):
        self.data = data
        self.scorer = scorer
        self.metrics = metrics
        self.out_metrics = {}
        
    def exec(self):
        run = wandb.init(reinit=True)
        config = wandb.config
        
        assert run is not None
        assert type(run) is wandb.sdk.wandb_run.Run
        
        x_train:StandardDataset = self.data
        
        for clazz in config.order:
            wrapper:BaseWrapper = Container.get_wrapper(clazz, config[clazz])
            wrapper.fit(x_train)
            
            x_train = wrapper.predict(x_train)

        m_wrapper = Container.get_metric(self.scorer)
        
        self.out_metrics[self.scorer] = m_wrapper.predict(x_train)
        
        for metric in self.metrics:
            m_wrapper = Container.get_metric(metric)
            try:
                self.out_metrics[metric] = m_wrapper.predict(x_train)
            except Exception as ex:
                print(traceback.print_exc())
        
    def log_metrics(self):
        wandb.log(self.out_metrics)
    
    def get_pipeline(self, name, config, train_dm):
        
        pl_conf = WandbRunPipelineModel(
            name=f'CrossValPipeline_{name}',
            train_input=train_dm,
            filters=[FilterModel(clazz=clazz, params=config[clazz]) for clazz in config["order"]],
            metrics=self.metrics
        )

        pipeline = Container.PIPELINES[pl_conf._clazz](pl_conf)
        pipeline.fit(train_dm)

        return pipeline


"""
TODO Todavía no se cómo tengo que hacer
"""   
class SupervisedRun:
    def __init__(self, train_data, test_data, scorer, metrics, group_name=None, run_name=None):
        self.train_data = train_data
        self.test_data = test_data
        self.scorer = scorer
        self.metrics = metrics
        self.group_name = group_name
        self.run_name = run_name
        self.out_metrics = {}
        
    def exec(self):
        config = wandb.config
        print(f'Config > {config}')
        run = wandb.init(group=self.group_name, name=self.run_name, reinit=True)
        assert run is not None
        assert type(run) is wandb.sdk.wandb_run.Run
        
        train_data = self.train_data
        test_data = self.test_data
        
        for clazz in config.order:
            wrapper:BaseWrapper = Container.get_wrapper(clazz, config[clazz])
            wrapper.fit(self.train_data)
            
            train_data = wrapper.predict(train_data)
            test_data = wrapper.predict(test_data)

        m_wrapper = Container.get_metric(self.scorer)
        
        self.out_metrics[self.scorer] = m_wrapper.predict(test_data)
        
        for metric in self.metrics:
            m_wrapper = Container.get_metric(metric)
            self.out_metrics[metric] = m_wrapper.predict(test_data)
        
    def get_pipeline(self, name, config):
        pipeline = []
        for clazz in config["order"]:
            wrapper:BaseWrapper = Container.get_wrapper(clazz, config[clazz])
            wrapper.fit(self.data)
            pipeline.append(wrapper)
        return pipeline
    
    def log_metrics(self):
        wandb.log(self.metrics)   

class ShuffleCVRun:
    def __init__(self, data, scorer, metrics=[], n_splits=2, test_size=0.2, random_state=7):
        self.data = data
        self.metrics = metrics
        self.scorer = scorer
        self.n_splits = n_splits
        self.test_size = test_size
        self.random_state = random_state
        self.out_metrics = {}
    
    def exec(self):
        run = wandb.init(reinit=True)
        
        assert run is not None
        assert type(run) is wandb.sdk.wandb_run.Run
        
        cv = ShuffleSplit(
            n_splits=self.n_splits, 
            test_size=self.test_size, 
            random_state=self.random_state
        )
        
        splits = cv.split(self.data)
        cv_name = randomname.get_name()
        
        for split,(train_idx, test_idx) in enumerate(splits):
        
            run_name = f"{cv_name}-{split:02}"
            group_name = f"cv_{cv_name}"
            
            train_data = self.data[train_idx]
            test_data = self.data[test_idx]
        
            s_run = SupervisedRun(train_data, test_data, group_name, run_name)
            s_run.exec()
            
            for k,v in s_run.metrics.items():
                m_acum = self.out_metrics.get(k, []) 
                m_acum.append(v)
                self.out_metrics[k] = m_acum
        
    def log_metrics(self):
        wandb.log(dict(map(lambda kv: (kv[0],np.mean(kv[1])), self.out_metrics.items())))
    
    def get_pipeline(self, name, config, train_dm):
        
        pl_conf = WandbRunPipelineModel(
            name=f'CrossValPipeline_{name}',
            train_input=train_dm,
            filters=[FilterModel(clazz=clazz, params=config[clazz]) for clazz in config["order"]],
            metrics=self.metrics
        )
        
        pipeline = Container.PIPELINES[pl_conf._clazz](pl_conf)
        pipeline.fit(train_dm)
        
        return pipeline

class RunEnum(Enum):
    unsupervised = UnsupervisedRun
    superised = SupervisedRun
    shuffle_cv = ShuffleCVRun