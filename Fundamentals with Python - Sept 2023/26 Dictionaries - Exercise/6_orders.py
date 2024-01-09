products = {}

while True:
    info = input()
    if info == "buy":
        break

    product_data = info.split()
    product_name = product_data[0]
    product_price = float(product_data[1])
    product_quantity = int(product_data[2])

    if product_name in products.keys():
        products[product_name][0] = product_price
        products[product_name][1] += product_quantity
    else:
        products[product_name] = [product_price,product_quantity]

for product_name, (price, quantity) in products.items():
    total_price = price * quantity
    print(f"{product_name} -> {total_price:.2f}")