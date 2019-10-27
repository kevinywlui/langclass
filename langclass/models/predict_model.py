import os
from pathlib import Path

import joblib

from langclass.features.build_features import Vectorizer

current_file_path = Path(os.path.realpath(__file__))
vecparams_model_path = (
    current_file_path.parent.parent.parent / "models" / "vecparams_model.pkl"
)


class Predictor:
    def __init__(self, vecparams_model_path):
        vec_params, self.model = joblib.load(vecparams_model_path)
        self.vectorizer = Vectorizer(**vec_params)

    def predict(self, code):
        vec_code = self.vectorizer(code)
        return self.model.predict([vec_code])[0]
