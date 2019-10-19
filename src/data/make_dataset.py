# This script is meant to be called from the Makefile.
#
# This script will generate csv files from the files in
# `data/external/RosettaCodeData`. There will be one csv file per programming
# language with header `['task', 'code']` where
#   - `task` is the programming task as describe here:
#     https://rosettacode.org/wiki/Category:Programming_Tasks,
#   - `code` is the source code used to solve that task.
# The csv files will be named LANGUAGE.csv where LANGUAGE will be determined
# from the folder names in `data/external/RosettaCodeData/Lang`.

import csv
import os
from pathlib import Path

# path of current file
file_path = Path(os.path.realpath(__file__))

# path of data directory
data_path = file_path.parent.parent.parent / "data"

# path of input (language directory of RosettaCodeData)
lang_path = data_path / "external" / "RosettaCodeData" / "Lang"

# path of output
output_path = data_path / "processed"

# header names
fieldnames = ["task", "code"]

# iterate over all folders
for lang_folder in lang_path.iterdir():
    # set the name
    lang_name = lang_folder.name
    csv_path = output_path / (lang_name + ".csv")

    # write the csv by iterating over all tasks
    with open(csv_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        task_folders = (x for x in lang_folder.iterdir() if x.is_dir())
        for task_folder in task_folders:
            task = task_folder.name
            for file in task_folder.iterdir():
                with open(file, "r") as f:
                    code = f.read()
                writer.writerow({"task": task, "code": code})
