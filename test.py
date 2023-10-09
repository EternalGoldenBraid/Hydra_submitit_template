"""
This file is not written in the style if it existing in /src/.
Instead it's assumed to be linked to /test.py.

This is due to the codebase that I wrote this for is not in the src/.. format.
"""
import os
os.umask(0000) # Allows us to remove files from nfs on when accessing outside node. # NOTE NOT NICE SOLUTION
import logging
log = logging.getLogger(__name__)
log.info("test.py runnig")
import time
from pathlib import Path

from omegaconf import DictConfig
import omegaconf
import hydra
import submitit

@hydra.main(version_base=None, config_path="config", config_name="config.yaml")
def main(config: DictConfig) -> None:

    ### Need to do imports within main due to containerization
    #import torch
    import numpy as np
    import mlflow
    from src.plot_test.gaussians import plot_gaussian

    log.info(f"list_dir: {os.listdir('.')}")
    log.info(f"list_dir_hydra: {os.listdir(hydra.utils.get_original_cwd())}")
    log.info(f"Path: {config.paths.logging_path}")
    
    
    mlflow.set_tracking_uri(config.logging.tracking_uri)
    mlflow.set_experiment(config.experiments.name)
    print("Tracking uri: ", config.logging.tracking_uri)
    with mlflow.start_run(description="Testing apptainer") as mlflow_run:
        log.info("Running")
        mlflow.log_param(key="key1", value=42)
        mlflow.log_param(key="name", value=config.experiments.name)

        # env = submitit.JobEnvironment()
        # log.info(f"Process ID {os.getpid()} executing task {config.experiments.name}, with {env}")
        
        train_dir:Path = Path(config.paths.train_dir)
        log.info(f"Data: {len([dir for dir in train_dir.glob('*') if dir.is_dir()])}")
        
        fig = plot_gaussian()
        mlflow.log_figure(fig, "gaussian.png")
        
if __name__ == '__main__':
    main()