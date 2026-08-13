import pandas as pd


def get_country_name(df):
    """Mapea códigos numéricos a nombres de países según el diccionario."""
    mapping = {
        1: "Australia", 2: "Austria", 3: "Belgium", 12: "unidentified",
        29: "Poland", 41: "United Kingdom", 42: "USA", 44: "com"
    }
    # Se recomienda completar el diccionario con los 47 códigos del archivo
    df['COUNTRY_NAME'] = df['COUNTRY'].map(mapping)
    return df


def clean_currency_data(df):
    """Valida que los precios sean positivos y no nulos."""
    df = df.dropna(subset=['PRICE'])
    df = df[df['PRICE'] > 0]
    return df


def segment_by_period(df, mes_inicio, mes_fin):
    """Filtra el DataFrame por el rango de meses (4-8)."""
    return df[(df['MONTH'] >= mes_inicio) & (df['MONTH'] <= mes_fin)]
