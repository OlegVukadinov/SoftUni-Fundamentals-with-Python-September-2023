total_price_without_taxes = 0

while True:
    command = input()

    if command == "special":
        if total_price_without_taxes == 0:
            print(f"Invalid order!")
            break
        else:
            print("Congratulations you've just bought a new computer!")
            print(f"Price without taxes: {total_price_without_taxes:.2f}$")
            print(f"Taxes: {(total_price_without_taxes * 0.20):.2f}$")
            print("-----------")
            print(f"Total price: {(total_price_without_taxes + total_price_without_taxes * 0.20) - ((total_price_without_taxes + total_price_without_taxes * 0.20) * 0.10):.2f}$")
            break

    elif command == "regular":
        if total_price_without_taxes == 0:
            print(f"Invalid order!")
            break
        else:
            print("Congratulations you've just bought a new computer!")
            print(f"Price without taxes: {total_price_without_taxes:.2f}$")
            print(f"Taxes: {(total_price_without_taxes * 0.20):.2f}$")
            print("-----------")
            print(f"Total price: {total_price_without_taxes + total_price_without_taxes * 0.20:.2f}$")
            break

    part_price = float(command)

    if part_price < 0:
        print("Invalid price!")
        continue
    total_price_without_taxes += part_price
