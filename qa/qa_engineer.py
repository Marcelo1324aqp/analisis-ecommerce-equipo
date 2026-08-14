def validate_page_flow(df):
    """
    Verifica que el número de página esté estrictamente entre 1 y 5.
    Retorna los registros que violan esta regla para auditoría.
    """
    invalid_pages = df[(df['PAGE'] < 1) | (df['PAGE'] > 5)]
    if invalid_pages.empty:
        return "QA Pass: Todas las páginas están en el rango 1-5."
    return f"QA Fail: Se encontraron {len(invalid_pages)} registros fuera de rango."


def check_location_distribution(df):
    """
    Valida que la ubicación de la foto (LOCATION) sea un valor entero del 1 al 6.
    Asegura que no existan nulos en esta métrica crítica.
    """
    valid_locations = [1, 2, 3, 4, 5, 6]
    issues = df[~df['LOCATION'].isin(valid_locations)]
    return {
        "is_valid": issues.empty,
        "null_count": df['LOCATION'].isnull().sum(),
        "invalid_entries": len(issues)
    }


def verify_model_photography(df):
    """
    Comprueba que la variable de fotografía solo contenga las categorías
    1 (en face) o 2 (profile).
    """
    counts = df['MODEL PHOTOGRAPHY'].value_counts().to_dict()
    isValid = all(k in [1, 2] for k in counts.keys())
    return f"Consistencia de fotografía: {'Correcta' if isValid else 'Error en categorías'}"
