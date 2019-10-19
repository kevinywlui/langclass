# This file provides method for vectorizing the input code

import re

import numpy as np
from sklearn.utils import murmurhash3_32


def alphanum_cont(string):
    nonalphanumerical = re.compile(r"([^a-zA-Z0-9])")
    split_code = string.split()
    tokens = []
    for part in split_code:
        for t in re.split(nonalphanumerical, part):
            if t:
                tokens.append(t)
    return tokens


class Vectorizer:
    def __init__(self, n_features=2 ** 10, n_gram=range(1, 2), tokenizer="char", hash_seed=0):
        self.n_features = n_features
        self.n_gram = n_gram

        self._tokenizer = self._make_tokenizer(tokenizer)
        self._hash = self._make_hash(n_features, hash_seed)

    def __call__(self, feature):
        vec = np.zeros(self.n_features)
        tokens = self._tokenizer(feature)

        for n in self.n_gram:
            for i in range(len(tokens) - n + 1):
                g = "".join(tokens[i : i + n])
                idx = self._hash(g)
                vec[idx] += 1
        norm = np.linalg.norm(vec)
        return vec / norm

    def _make_tokenizer(self, tokenizer):
        if callable(tokenizer):
            return tokenizer

        if tokenizer == "char":
            identity = lambda x: x
            return identity

    def _make_hash(self, n_features, hash_seed):
        f = lambda x: murmurhash3_32(x, seed=hash_seed) % n_features
        return f
