import re

info = {}
pattern = r"%([A-Z][a-z]+)%([^\|\$\%\.]*?)<(\w+)>([^\|\$\%\.]*?)\|([0-9]+)\|([^\|\$\%\.]*?)([0-9.]+[0-9]?)\$"     #r"%([A-Z][a-z]*)%<(\w+)>\|(\d+)\|(\d+\.\d+?)\$"
total_price = 0
total_income = 0

while True:
    line = input()
    if line == "end of shift":
        print(f"Total income: {total_income:.2f}")
        break

    match = re.search(pattern, line)
    if match:
        customer_name = match.group(1)
        product_name = match.group(3)
        quantity = match.group(5)
        price = match.group(7)

        total_price += float(price) * int(quantity)
        total_income += total_price
        print(f"{customer_name}: {product_name} - {total_price:.2f}")
        total_price = 0