# This file holds the model class which helps abstract away from pre/post
# processing.

import numpy as np
from sklearn.preprocessing import LabelEncoder


class Model:
    def __init__(self, model, vectorizer):
        self.model = model
        self.label_encoder = LabelEncoder()
        self.feature_dict = dict()

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
        enc_y = self.model.predict([vec_x])
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
