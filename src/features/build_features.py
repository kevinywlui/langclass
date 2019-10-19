# This file provides method for vectorizing the input code

from sklearn.utils import murmurhash


class Vectorizer():
    def __init__(n_features=2**10, n_gram=(1, 1), tokenizer=None, hash_seed=0):
        self.n_features = n_features
        self.n_gram = n_gram
        self.tokenizer = tokenizer
        self.hash_seed = hash_seed

    def __call__(feature):
