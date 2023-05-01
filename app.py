"""python modeule for basic app hosting"""

import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler

from src.model_deployment import load_model, read_model

application=Flask(__name__)

app=application

# initialize the model from wandb model regsitry

lenet_model =  read_model()
print("Model Summary : ",lenet_model)

## Route for a home page
@app.route('/')
def index():
    return render_template('index.html') 


if __name__=="__main__":
    # host the appication inside port 8080   
    app.run(host='0.0.0.0', port=8080)        


