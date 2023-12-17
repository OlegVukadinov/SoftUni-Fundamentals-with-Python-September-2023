def total_price(product, quantity):
    if product == "coffee":
        tot_price = quantity * 1.50
    elif product == "water":
        tot_price = quantity * 1.00
    elif product == "coke":
        tot_price = quantity * 1.40
    elif product == "snacks":
        tot_price = quantity * 2.00
    return tot_price

text = input()
number = int(input())

print(f"{total_price(text, number):.2f}")