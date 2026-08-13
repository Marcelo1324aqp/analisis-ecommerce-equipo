import pandas as pd


def cargar_datos(ruta_archivo):
    """
    Lee el dataset de e-shop clothing 2008.
    Argumentos: ruta_archivo (str)
    Retorna: DataFrame de pandas
    """
    try:
        # El archivo usa punto y coma como separador
        df = pd.read_csv(ruta_archivo, sep=';')
        # Estandarizamos los nombres de columnas a MAYÚSCULAS,
        # porque el CSV real las trae en minúsculas y el resto
        # de las funciones del equipo las espera en mayúsculas.
        df.columns = [c.upper() for c in df.columns]
        print("Datos cargados exitosamente.")
        return df
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None


if __name__ == "__main__":
    df = cargar_datos("e-shop clothing 2008.csv")
    if df is not None:
        print(df.head())
        print("Columnas disponibles:", list(df.columns))
