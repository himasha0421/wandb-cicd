import os
from urllib.parse import urlencode

import wandb

assert os.environ['WANDB_API_KEY'] , "You must set the wandb client api key !!!!"
#define other first citizen params
ENTITY = os.getenv('ENTITY') or 'himasha'
PROJECT = os.getenv('PROJECT') or 'mnist-experiment'
MODEL_TAG = os.getenv('WANDB_TAG') or 'production-candidate'
RUN_ID =  os.getenv('RUN_ID')
MODEL_REGISTRY = os.getenv('REGISTRY') or 'mnist-registry'

# init wandb client
api = wandb.Api()
run = api.run(f"{ENTITY}/{PROJECT}/{RUN_ID}")
registry_path = f'{ENTITY}/model-registry/{MODEL_REGISTRY}'

def model_migrate():
    """this method is to migrate experimental model to registry staging"""

    # get the model from the artifacts registry and promote to the model registry
    art = [a for a in run.logged_artifacts() if a.type == 'model']

    # below code part related to get the model artifact tagged with run and link to a existing model registry
    if art:
        assert len(art) == 1, 'More then 1 artifact of type model!'
        art[0].link(registry_path , aliases=[MODEL_TAG])

    # generate the url for the linked model
    versions = api.artifact_versions('model', registry_path)
    # visualize all the versions inside the registry
    for v in versions:
        print(f'Model version: {v.version} with tags: {v.aliases}')

    # get the latest model
    latest_model = versions[0]

    # generate the model url to quick look
    query = urlencode({'selectionPath': registry_path, 'version': latest_model.version})
    registry_url = f'https://wandb.ai/{latest_model.entity}/registry/model?{query}'
    
    print(f"Latest Production candidate model registry url : {registry_url}")

    # to add this url to pr comment 
    with open( os.environ['GITHUB_OUTPUT'] , 'a' ) as f:
        print( f'MODEL_URL={registry_url}' , file=f )


if __name__ == '__main__':
    # excute the model migration
    model_migrate()