# Biblioteca: Validation
# Funções de validação de dados

def validate_schema(df, expected_columns):
    actual = set(df.columns)
    missing = set(expected_columns) - actual
    if missing:
        raise ValueError(f"Colunas ausentes: {missing}")
    return True
