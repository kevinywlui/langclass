# This module contains just one function which returns the data as a pandas
# dataframe.

import pandas as pd
import os
from pathlib import Path

file_path = Path(os.path.realpath(__file__))
data_path = file_path.parent.parent.parent / "data" / "processed" / "data.csv"

def get_df():
    return pd.read_csv(data_path)