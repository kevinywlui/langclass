# This script will make a single prediction. HIGHLY INEFFICIENT if you want to
# make multiple predictions since each prediction will load the model.

import joblib
from langclass.features.build_features import Vectorizer

import os
from pathlib import Path

current_file_path = Path(os.path.realpath(__file__))
vecparams_model_path = current_file_path.parent.parent

print(vecparams_model_path)
 def predict(code)
#     params, model = joblib
