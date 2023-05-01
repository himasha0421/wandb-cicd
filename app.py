"""python modeule for basic app hosting"""

import numpy as np
import pandas as pd
import torch
from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler

from src.model import ConvNet

application=Flask(__name__)

app=application

# initialize the model from wandb model regsitry
# define model configs
model_config = {"hidden_layer_sizes": [32, 64],
            "kernel_sizes": [3],
            "activation": "ReLU",
            "pool_sizes": [2],
            "dropout": 0.5,
            "num_classes": 10}

# initialize the conv model
lenet_model = ConvNet(**model_config)
# load the trained weights from checkpoint
lenet_model.load_state_dict(torch.load("model_artifacts/lenet.pt",map_location='cpu'))

print("Model Summary : ",lenet_model)

## Route for a home page
@app.route('/')
def index():
    return render_template('index.html') 


if __name__=="__main__":
    # host the appication inside port 8080   
    app.run(host='0.0.0.0', port=8080)        


