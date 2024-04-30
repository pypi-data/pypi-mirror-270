import pandas as pd
import os

def get_data():
    data_path = os.path.join(os.path.dirname(__file__), 'cmp1.csv')
    print(f"Attempting to read CSV from: {data_path}")
    data = pd.read_csv(data_path)
    print(data.columns.tolist())  # This prints the list of headers
    return pd.read_csv(data_path)

get_data()