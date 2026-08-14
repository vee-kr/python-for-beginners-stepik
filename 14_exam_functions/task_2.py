def get_shipping_cost(quantity):
    total = 1000 + (quantity - 1) * 120
    return total


quantity = int(input())
print(get_shipping_cost(quantity))
