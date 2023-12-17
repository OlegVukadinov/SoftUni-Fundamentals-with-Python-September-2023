vehicles_list = input().split(">>")

total_tax = 0

for curr_car in vehicles_list:
    token = curr_car.split()
    car_type = token[0]
    years = float(token[1])
    kilometers = float(token[2])

    if car_type == "family":
        init_car_tax = 50
        raise_money = kilometers // 3000
        tax_for_curr_car = raise_money * 12 + (init_car_tax - years * 5)
        total_tax += tax_for_curr_car
        print(f"A {car_type} car will pay {tax_for_curr_car:.2f} euros in taxes.")
    elif car_type == "heavyDuty":
        init_car_tax = 80
        raise_money = kilometers // 9000
        tax_for_curr_car = raise_money * 14 + (init_car_tax - years * 8)
        total_tax += tax_for_curr_car
        print(f"A {car_type} car will pay {tax_for_curr_car:.2f} euros in taxes.")
    elif car_type == "sports":
        init_car_tax = 100
        raise_money = kilometers // 2000
        tax_for_curr_car = raise_money * 18 + (init_car_tax - years * 9)
        total_tax += tax_for_curr_car
        print(f"A {car_type} car will pay {tax_for_curr_car:.2f} euros in taxes.")
    else:
        print("Invalid car type.")
# print(f"A {car_type} car will pay {tax_for_curr_car} euros in taxes.")
print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")
