"""this file for load the model from wandb model regsirty related to production"""

import os
from urllib.parse import urlencode

import torch
import wandb

from model import ConvNet


def load_model(entity='himasha',
               project='mnist-experiment',
               model_regsitry='mnist-registry',
               tag='production-candidate'
               ):
    
    # set the env variables
    assert os.environ['WANDB_API_KEY'] , "You must set the wandb client api key !!!!"
    ENTITY = os.getenv('ENTITY') or entity
    PROJECT = os.getenv('PROJECT') or project
    REGISTRY = os.getenv('REGISTRY') or model_regsitry
    TAG = os.getenv('TAG') or tag

    # init the wandb api
    wandb_api = wandb.Api()
    # load th eproduction candidate model from regsitry and test out
    model_path = f'{ENTITY}/model-registry/{REGISTRY}:{TAG}'
    wandb_api.artifact(model_path).download("model_artifacts")

if __name__ == '__main__':
    # load the model
    load_model()



