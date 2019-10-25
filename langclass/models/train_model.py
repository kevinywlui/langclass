# This file trains and save the model.
# TODO: support more ways to train

import os
from pathlib import Path

import lightgbm as lgb
from langclass.data.dataframes import Data
from langclass.features.build_features import Vectorizer

import joblib

current_file_path = Path(os.path.realpath(__file__))
vecparams_model_path = (
    current_file_path.parent.parent / "models" / "vecparams_model.pkl"
)


def main():
    data = Data()
    train_df = data.train_df
    X_train = train_df["code"]
    y_train = train_df["language"]

    params = {"n_gram": (2, 2), "tokenizer": "char"}
    vec = Vectorizer(**params)

    X_train_vec = vec.vectorize_df(X_train)

    model = lgb.LGBMClassifier(n_estimators=150)
    model.fit(X_train_vec, y_train)
    vecparams_model = (params, model)
    joblib.dump(vecparams_model, "vecparams_model.pkl")


if __name__ == "__main__":
    main()
