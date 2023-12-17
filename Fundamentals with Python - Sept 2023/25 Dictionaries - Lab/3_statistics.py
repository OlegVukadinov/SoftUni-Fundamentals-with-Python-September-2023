products_stock = {}

while True:
    command = input()
    if command == "statistics":
       break
    food_data = command.split(": ")
    product = food_data[0]
    quantity = int(food_data[1])

    if product in products_stock:
        products_stock[product] += int(quantity) # ако продукта вече го има в речника добавяме новите бройки
    else:
        products_stock[product] = int(quantity)  # ако го нямя го добявяме в речника

product_count = len(products_stock) # защото в речника има само разл продукти
total_quantity = sum(products_stock.values())

print("Products in stock:")

for product, quantity in products_stock.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {product_count}")
print(f"Total Quantity: {total_quantity}")
