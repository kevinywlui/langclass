# This file holds the model class which helps abstract away from pre/post
# processing.

import numpy as np
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from pathlib import Path

from language_source_classifier.features.build_features import Vectorizer


class Model:
    def __init__(
        self,
        model,
        n_features=2 ** 10,
        n_gram=range(1, 2),
        tokenizer="char",
        hash_seed=0,
        build_hash_dict=False,
    ):
        self.model = model
        self.vectorizer = Vectorizer(
            n_features=n_features,
            n_gram=n_gram,
            tokenizer=tokenizer,
            hash_seed=hash_seed,
            build_hash_dict=build_hash_dict,
        )
        self.label_encoder = LabelEncoder()

    # this needs a new name
    def vec(self, X):
        """Return the vectorized version of `X` using `self.vectorize`.

        Args:
            X: pandas series whose entries will be vectorized

        Returns:
            2d-numpy array whose rows are the vectorized-rows of X.
        """
        v_list = []
        for _index, value in X.items():
            v_list.append(self.vectorizer(value))
        return np.array(v_list)

    def y_dec(self, y_enc):
        """Decode `y_enc` by applying the inverse transform of the label
        encoder.

        Args:
            y_enc: An integer to be decoded.
        
        Returns:
            The corresponding label of y_dec.
        """
        return self.label_encoder.inverse_transform([y_enc])[0]

    def predict(self, x):
        """Return the prediction.

        Args:
            x: Input

        Returns:
            The predict of the y-value given this input.
        """
        vec_x = self.vectorizer(x)
        y_enc = self.model.predict([vec_x])
        y = self.y_dec(y_enc)
        return y

    def fit(self, X, y, *args, **kwargs):
        """Fit the model.

        Args:
            X: pd.Series of inputs
            y: pd.Series of labels
            *args: arguments to be passed to model.fit
            **kwargs: keyword-arguments to be passed to model.fit
        """
        vec_X = self.vec(X)
        enc_y = self.label_encoder.fit_transform(y)
        self.model.fit(vec_X, enc_y, *args, **kwargs)
        return

    def save(self, path, overwrite=False):
        """Save a pickled version of the model using joblib.

        Args:
            path: the path the pickle will be saved to.
            overwrite: boolean determining whether we overwrite
        """
        path = Path(path)
        if path.exists() and not overwrite:
            raise FileExistsError('attempting to save pickle to an existing file')
        joblib.dump(self.model, path)
        return

    def evaluate(self, X, y):
        """Evaluate the accuracy of this model using a test set.

        Args:
            X: pd.Series of inputs
            y: pd.Series of labels

        Returns:
            a float representing the accuracy
        """
        vec_X = self.vec(X)
        y_pred = self.model.predict(vec_X)
        y_enc = self.label_encoder.transform(y)
        return accuracy_score(y_enc, y_pred)
