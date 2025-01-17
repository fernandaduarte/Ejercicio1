# Importar librerías necesarias
import pandas as pd

# Modulo 1: Lectura de datos  
def cargar_datos(ruta_csv):
    """
    Carga los datos desde un archivo CSV.
    
    Args:
        ruta_csv (str): Ruta al archivo CSV.
        
    Returns:
        pd.DataFrame: DataFrame con los datos cargados.
    """
    try:
        datos = pd.read_csv(ruta_csv)
        print("Datos cargados correctamente.")
        return datos
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None