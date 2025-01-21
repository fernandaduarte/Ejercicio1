# Modulo 4: Visualización de datos

import folium

def generar_mapa(datos, nombre_mapa="mapa.html"):
    """
    Genera un mapa interactivo con los datos de GPS.
    
    Args:
        datos (pd.DataFrame): DataFrame con las columnas "latitude" y "longitude".
        nombre_mapa (str): Nombre del archivo HTML a guardar.
    """
    try:
        # Crear un mapa centrado en el primer punto
        centro = [datos["lat"].iloc[0], datos["lon"].iloc[0]]
        mapa = folium.Map(location=centro, zoom_start=12)
        
        # Agregar puntos al mapa
        for _, fila in datos.iterrows():
            folium.Marker([fila["lat"], fila["lon"]]).add_to(mapa)
        
        # Guardar el mapa como archivo HTML
        mapa.save(nombre_mapa)
        print(f"Mapa generado y guardado como {nombre_mapa}")
    except Exception as e:
        print(f"Error al generar el mapa: {e}")
