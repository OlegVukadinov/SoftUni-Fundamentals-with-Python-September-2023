items = input().split("|")
budget = float(input())

profit = 0
bought_items = []

for item in items:
    item_type, item_price = item.split("->")
    item_price = float(item_price)
    if item_type == "Clothes" and item_price > 50.00:
        continue
    elif item_type == "Shoes" and item_price > 35.00:
        continue
    elif item_type == "Accessories" and item_price > 25.50:
        continue
    if budget >= item_price:
        current_profit = item_price * 0.40
        profit += current_profit
        budget -= item_price
        bought_items.append(item_price + current_profit)

for element in bought_items:
    print(f"{element:.2f}", end=' ')

print()
print(f"Profit: {profit:.2f}")

budget += sum(bought_items)

if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

