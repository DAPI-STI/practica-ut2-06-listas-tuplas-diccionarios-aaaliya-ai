"""
EX06 (Compendio: listas + tuplas + diccionarios)
Ticket de compra: calcula coste por producto y total general.
"""

PRICES: dict[str, float] = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}

def checkout(cart: list[tuple[str, int]]) -> tuple[dict[str, float], float]:
    costs = {}
    total = 0.0

    for product, units in cart:
        if units < 0:
            raise ValueError("Las unidades no pueden ser negativas")

        if product not in PRICES:
            raise ValueError(f"Producto no existente: {product}")

        cost = round(PRICES[product] * units, 2)

        if product in costs:
            costs[product] = round(costs[product] + cost, 2)
        else:
            costs[product] = cost

        total = round(total + cost, 2)

    return costs, total