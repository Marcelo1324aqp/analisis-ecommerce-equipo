import pandas as pd


def calculate_conversion_rate(df):
    """Compara clics en categoría 'sale' (4) vs categorías regulares."""
    sale_clicks = len(df[df['PAGE 1 (MAIN CATEGORY)'] == 4])
    regular_clicks = len(df[df['PAGE 1 (MAIN CATEGORY)'].isin([1, 2, 3])])
    return {"sale_clicks": sale_clicks, "regular_clicks": regular_clicks}


def analyze_price_elasticity(df):
    """Compara clics entre productos con precio superior al promedio (1) y el resto (2)."""
    return df['PRICE 2'].value_counts()


def identify_session_depth(df):
    """Encuentra las sesiones con la secuencia de clics (ORDER) más larga."""
    return df.groupby('SESSION ID')['ORDER'].max().sort_values(ascending=False)


def color_popularity_by_category(df):
    """Determina el color más frecuente por categoría de prenda."""
    return df.groupby('PAGE 1 (MAIN CATEGORY)')['COLOUR'].agg(pd.Series.mode)
