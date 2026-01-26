"""
EX03 (Tuplas)
Devolver el mínimo y el máximo de una lista.
"""

def min_max_prices(prices: list[float]) -> tuple[float, float]:
    """
    Devuelve una tupla (mínimo, máximo).

    - Si prices está vacía, lanza ValueError.
    """
    if not prices:
        raise ValueError("La lista de precios está vacía")

    return min(prices), max(prices)


# Pruebas
print(min_max_prices([10.5, 3.2, 8.0, 15.1]))
print(min_max_prices([5.0]))
