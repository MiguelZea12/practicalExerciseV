from src.data_loader import load_data
from src.visualization import create_visualizations

def main():
    # Cargar datos
    file_path = 'mnt/data/Cleaned_Student_Depression_Dataset_for_Analysis.csv'
    df = load_data(file_path)

    # Crear visualizaciones
    create_visualizations(df)

if __name__ == "__main__":
    main()
