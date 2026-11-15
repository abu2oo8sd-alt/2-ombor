
def find_top_seller(products: dict, sales: dict) -> str:
    max_revenue = 0
    top_product = ""

    for product, price in products.items():
        revenue = price * sales[product]

        if revenue > max_revenue:
            max_revenue = revenue
            top_product = product

    return top_product


print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10, "Banan": 5, "Uzum": 8}
))
