# 178.py
# Topic: Reading a CSV file with the csv module
#
# os.path.dirname(os.path.abspath(__file__)) = the folder of THIS
# script (works no matter where you run from). csv.reader parses
# each row into a list. next(reader) skips the header line, then
# we print column 0 and 1 separated by |.

import csv
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'TD.csv')

with open(file_path) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row
    for col in reader:
        print(col[0], col[1], sep="|")