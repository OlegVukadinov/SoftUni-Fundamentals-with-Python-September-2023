number_of_orders = int(input())
total_price = 0
for current_order in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    caps_per_day = int(input())

    if not 0.01 <= price_per_capsule <= 100.00:
        continue
    if not 1 <= days <= 31:
        continue
    if not 1 <= caps_per_day <= 2000:
        continue
    price = price_per_capsule * caps_per_day * days
    total_price += price

    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")