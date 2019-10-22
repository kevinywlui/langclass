# This file holds the model class which helps abstract away from pre/post
# processing.

from sklearn.preprocessing import LabelEncoder
import numpy as np

class Model():
    def __init__(self, model, vectorizer):

        self.np_vectorizer = np.vectorize(vectorizer)

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
        for index, value in X.items():




    def y_dec(self, y_enc):
        """Decode `y_enc` by applying the inverse transform of the label
        encoder.
        """
        return self.label_encoder.inverse_transform([y_enc])[0]

    def predict(self, x):
        """Return the prediction.
        """
        vec_x = self.vectorizer(x)
        enc_y = self.model.predict([vec_x])
        y = self.y_dec(y_enc)
        return y

    def fit(self, X, y, *args, **kwargs):
        """Fit the model.
        """
        vec_X = f(X)
        enc_y = self.label_encoder.fit_transform(y)
        self.model.fit(vec_X, enc_y, *args, **kwargs)
        return
