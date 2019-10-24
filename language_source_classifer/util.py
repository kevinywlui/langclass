# Various utility functions

from collections import defaultdict


def codedict_mean(*args):
    # codedict maps code to the list of feature importance of the hashes
    codedict = defaultdict(list)
    for hash_dict, feature_importance in args:
        for key in hash_dict:
            for x in hash_dict[key]:
                codedict[x].append(feature_importance[key])

    n = len(args)
    codedict_mean = []
    for x in codedict:
        prod = 1
        for i in range(n):
            prod *= codedict[x][i]
        codedict_mean.append(prod ** (1 / n))
    return codedict_mean
