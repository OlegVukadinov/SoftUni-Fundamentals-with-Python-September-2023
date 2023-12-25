number_lines = int(input())
tank_capacity = 255
counter_liters = 0
for current_number_lines in range(1, number_lines + 1):
    liters = int(input())

    if liters <= tank_capacity:
        counter_liters += liters
        tank_capacity -= liters
    elif counter_liters > tank_capacity or liters > tank_capacity:
        print("Insufficient capacity!")
        continue
print(f"{counter_liters}")