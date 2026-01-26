"""
EX05 (Diccionarios)
Tabla de búsqueda: divisa -> símbolo.
"""

CURRENCIES: dict[str, str] = {"Euro": "€", "Dollar": "$", "Yen": "¥"}

def currency_symbol(currency: str) -> str | None:
    symbols = {
        "Euro": "€",
        "Dólar": "$",
        "Libra": "£",
        "Yen": "¥",
    }

    return symbols.get(currency)


