import joblib
import matplotlib as plt
import pandas as pd
import numpy as np
import os
from sklearn.ensemble import RandomForestRegressor
 
curr_path = os.path.dirname(os.path.realpath(__file__))
joblib_file = '/joblib_rf_reddit.pkl'
joblib_file = '/joblib_rf_reddit_.pkl.compressed'
#feat_cols = ['num_comments', 'polarity_score_title', 'polarity_score_text']
model = joblib.load(curr_path + joblib_file) 

def predict_upvote(attributes: np.ndarray):
    """ Reddit upvote predictions """
    pred = model.predict(attributes)
    return int(pred[0])



