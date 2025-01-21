# Modulo 3: Análisis de datos
import pandas as pd

def calcular_distancia_promedio(datos):
    """
    Calcula la distancia promedio entre puntos consecutivos.
    
    Args:
        datos (pd.DataFrame): DataFrame con las columnas "latitude" y "longitude".
        
    Returns:
        float: Distancia promedio en kilómetros.
    """
    from geopy.distance import geodesic
    
    try:
        distancias = []
        for i in range(len(datos) - 1):
            coord1 = (datos.iloc[i]["lat"], datos.iloc[i]["lon"])
            coord2 = (datos.iloc[i + 1]["lat"], datos.iloc[i + 1]["lon"])
            distancias.append(geodesic(coord1, coord2).kilometers)
        
        promedio = sum(distancias) / len(distancias)
        print(f"Distancia promedio: {promedio:.2f} km")
        return promedio
    except Exception as e:
        print(f"Error al calcular distancias: {e}")
        return None
