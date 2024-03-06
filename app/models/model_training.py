# model_training.py

import numpy as np
import pickle
from .model_definition import create_model

def train_and_save(features, labels):
    model = create_model()
    model.fit(features, labels)
    
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    return model
