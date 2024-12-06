import pandas as pd

def load_data(file_path: str):
    # Cargar el DataFrame
    df = pd.read_csv(file_path)
    return df
