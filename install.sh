#!/bin/bash

conda_env="apptainer_env"
conda create -n $conda_env python==3.8.13 -y
conda env config vars set -n $conda_env PIP_REQUIRE_VIRTUALENV=false

conda install -n $conda_env  \
	-c pytorch -c conda-forge \
	hydra-submitit-launcher==1.2.0 submitit==1.5.0 mlflow hydra-core omegaconf \
 	numpy \
	--y 

#	pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 \
#	cudatoolkit=11.3 \
