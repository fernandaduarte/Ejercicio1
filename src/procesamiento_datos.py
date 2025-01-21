# Modulo 2: Procesamiento y limpieza de datos
import pandas as pd

def procesar_datos(datos):
    """
    Limpia y procesa los datos.
    
    Args:
        datos (pd.DataFrame): DataFrame con los datos a procesar.
        
    Returns:
        pd.DataFrame: DataFrame con los datos procesados.
    """
    try:
        # Eliminar filas con valores nulos
        datos = datos.dropna(subset=["lat", "lon"])
        
        # Convertir coordenadas a tipo float
        datos["lat"] = datos["lat"].astype(float)
        datos["lon"] = datos["lon"].astype(float)
        
        print("Datos procesados correctamente.")
        return datos
    except Exception as e:
        print(f"Error al procesar los datos: {e}")
        return None
