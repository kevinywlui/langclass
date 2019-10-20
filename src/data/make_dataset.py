# This script is meant to be called from the Makefile.
#
# This script will generate a single csv to intended to be used as a final
# dataset. An example invocation of the script is
#   `python make_dataset.py Python, Ruby, C
# 
# The resulting result csv file will have header `['language', 'code']`, where
#   - `language` is either Python, Ruby, or C,
#   - `code` is a code snippet

import csv
import os
import sys
from pathlib import Path

# path of current file
file_path = Path(os.path.realpath(__file__))

# path of data directory
data_path = file_path.parent.parent.parent / "data"

# path of input (language directory of RosettaCodeData)
lang_path = data_path / "external" / "RosettaCodeData" / "Lang"

# path of output
output_file = data_path / "processed" / "data.csv"

# languages used
langs = sys.argv[1:]

# header names
fieldnames = ["language", "code"]

with open(output_file, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for lang in langs:
        lang_folder = lang_path / lang
        task_folders = (x for x in lang_folder.iterdir() if x.is_dir())
        for task_folder in task_folders:
            task = task_folder.name
            for file in task_folder.iterdir():
                with open(file, "r") as f:
                    code = f.read()
                if code:
                    writer.writerow({"language": lang, "code": code})
