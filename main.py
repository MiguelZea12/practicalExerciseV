from src.cargar_datos import cargar_datos
from src.visualizacion import crear_visualizaciones

def main():
    # Cargar datos
    ruta_archivo = 'mnt/data/Cleaned_Student_Depression_Dataset_for_Analysis.csv'
    df = cargar_datos(ruta_archivo)

    # Crear visualizaciones
    crear_visualizaciones(df)

if __name__ == "__main__":
    main()
