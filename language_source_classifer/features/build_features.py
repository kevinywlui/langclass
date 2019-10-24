# This file provides method for vectorizing the input code

import re
from collections import defaultdict

import numpy as np
from sklearn.utils import murmurhash3_32


def alphanum(string):
    nonalphanumerical = re.compile(r"([^a-zA-Z0-9])")
    split_code = string.split()
    tokens = []
    for part in split_code:
        for t in re.split(nonalphanumerical, part):
            if t:
                tokens.append(t)
    return tokens


class Vectorizer:
    def __init__(
        self,
        n_features=2 ** 10,
        n_gram=range(1, 2),
        tokenizer="char",
        hash_seed=0,
        build_hash_dict=False,
    ):
        self.n_features = n_features
        self.n_gram = n_gram

        self._tokenizer = self._make_tokenizer(tokenizer)
        self.hash = self.make_hash(n_features, hash_seed)

        self.build_hash_dict = build_hash_dict
        self.hash_dict = defaultdict(set)

    def __call__(self, feature):
        vec = np.zeros(self.n_features)
        tokens = self._tokenizer(feature)

        for n in self.n_gram:
            for i in range(len(tokens) - n + 1):
                g = "".join(tokens[i : i + n])
                idx = self.hash(g)
                vec[idx] += 1
                if self.build_hash_dict:
                    self.hash_dict[idx].add(g)
        norm = np.linalg.norm(vec)
        if norm > 0:
            return vec / norm
        else:
            return vec

    def vectorize_df(self, df):
        """Return the vectorized version of `df` using `self.vectorize`.

        Args:
            df: pandas series whose entries will be vectorized

        Returns:
            2d-numpy array whose rows are the vectorized-rows of df.
        """
        v_list = []
        for _index, value in df.items():
            v_list.append(self(value))
        return np.array(v_list)

    def _make_tokenizer(self, tokenizer):
        if callable(tokenizer):
            return tokenizer
        if tokenizer == "char":
            identity = lambda x: x
            return identity
        if tokenizer == "alphanum":
            return alphanum

    def make_hash(self, n_features, hash_seed):
        f = lambda x: murmurhash3_32(x, seed=hash_seed) % n_features
        return f
