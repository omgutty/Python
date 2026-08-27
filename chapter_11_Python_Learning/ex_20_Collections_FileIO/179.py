# 179.py
# Topic: Reading CSV with pandas
#
# pandas reads the whole CSV into a DataFrame (a table) and prints
# it nicely. Needs: pip install pandas. Same TD.csv as 178.py -
# compare the plain csv module (178) vs pandas (179).

import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'TD.csv')

df = pd.read_csv(file_path)
print(df)