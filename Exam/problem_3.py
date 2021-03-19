def delivery_products(products, args):
    products.extend(args)
    return products


def sell_products(products, args):
    if not args:
        products.pop(0)
    elif isinstance(args[0], int):
        product_to_sell = args[0]
        products = products[product_to_sell:]
    else:
        products = [item for item in products if item not in args]

    return products


def stock_availability(products, command, *args):

    if command == 'delivery':
        products = delivery_products(products, args)
    elif command == 'sell':
        products = sell_products(products, args)

    return products


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
