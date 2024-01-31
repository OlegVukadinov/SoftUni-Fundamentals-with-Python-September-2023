total_price_without_taxes = 0

while True:
    command = input()

    if command == "special":
        if total_price_without_taxes > 0:
            print(f"Congratulations you've just bought a new computer!")
            print(f"Price without taxes: {total_price_without_taxes:.2f}$")
            print(f"Taxes: {(total_price_without_taxes * 0.20):.2f}$")
            print("-----------")
            print(f"Total price: {(total_price_without_taxes - total_price_without_taxes * 0.10) * 1.2:.2f}$")
            break
        else:
            print("Invalid order!")
            break

    if command == "regular":
        if total_price_without_taxes > 0:
            print(f"Congratulations you've just bought a new computer!")
            print(f"Price without taxes: {total_price_without_taxes:.2f}$")
            print(f"Taxes: {(total_price_without_taxes * 0.20):.2f}$")
            print("-----------")
            print(f"Total price: {(total_price_without_taxes * 1.2):.2f}$")
            break
        else:
            print("Invalid order!")
            break
    part_prices = float(command)
    total_price_without_taxes += part_prices

    if part_prices < 0:
        print("Invalid price!")
        total_price_without_taxes -= part_prices
        continue
