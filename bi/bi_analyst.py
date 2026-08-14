import pandas as pd


def sales_funnel_analysis(df):
    """Analiza la pérdida de usuarios entre las páginas 1 y 5 de la tienda."""
    return df['PAGE'].value_counts().sort_index()


def price_impact_by_location(df):
    """Relaciona la ubicación de la foto (1-6) con el interés en productos caros."""
    return pd.crosstab(df['LOCATION'], df['PRICE 2'])


def conversion_by_photography_type(df):
    """Compara el rendimiento de fotos 'en face' (1) vs 'profile' (2)."""
    return df.groupby('MODEL PHOTOGRAPHY')['ORDER'].count()
