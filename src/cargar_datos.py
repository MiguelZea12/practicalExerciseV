import pandas as pd

def cargar_datos(ruta_archivo: str):
    # Cargar el DataFrame
    df = pd.read_csv(ruta_archivo)
    return df
