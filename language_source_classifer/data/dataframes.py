# This module contains just one function which returns the data as a pandas
# dataframe.

import os
from pathlib import Path
from sklearn.model_selection import train_test_split

import pandas as pd

file_path = Path(os.path.realpath(__file__))
data_path = file_path.parent.parent.parent / "data" / "processed" / "data.csv"

class Data():
    def __init__(self):
        self.full_df = pd.read_csv(data_path)
        self.train_df, self.test_df = train_test_split(self.full_df, random_state=0)