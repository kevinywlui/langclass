# This script will make a single prediction. HIGHLY INEFFICIENT if you want to
# make multiple predictions since each prediction will load the model.

import os
import sys
from pathlib import Path

import joblib

from langclass.features.build_features import Vectorizer

current_file_path = Path(os.path.realpath(__file__))
vecparams_model_path = (
    current_file_path.parent.parent.parent / "models" / "vecparams_model.pkl"
)


def predict():
    code = sys.argv[1]
    params, model = joblib.load(vecparams_model_path)
    vec = Vectorizer(**params)
    print(model.predict([vec(code)])[0])
