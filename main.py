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


from arch.data_architect import get_country_name, clean_currency_data, segment_by_period
from back.backend_developer import (
    calculate_conversion_rate, analyze_price_elasticity,
    identify_session_depth, color_popularity_by_category
)
from bi.bi_analyst import (
    sales_funnel_analysis, price_impact_by_location, conversion_by_photography_type
)
from qa.qa_engineer import validate_page_flow, check_location_distribution, verify_model_photography

if __name__ == "__main__":
    df = cargar_datos("e-shop clothing 2008.csv")

    # --- Data Architect ---
    df = clean_currency_data(df)
    df = get_country_name(df)
    print("\n--- Países mapeados ---")
    print(df[['COUNTRY', 'COUNTRY_NAME']].drop_duplicates().head())

    # --- Backend Developer ---
    print("\n--- Tasa de conversión Sale vs Regular ---")
    print(calculate_conversion_rate(df))
    print("\n--- Elasticidad de precio ---")
    print(analyze_price_elasticity(df))

    # --- BI Analyst ---
    print("\n--- Embudo de ventas por página ---")
    print(sales_funnel_analysis(df))
    print("\n--- Impacto de ubicación de foto en precio ---")
    print(price_impact_by_location(df))

    # --- QA Engineer ---
    print("\n--- Validación QA ---")
    print(validate_page_flow(df))
    print(check_location_distribution(df))
