number_lines = int(input())
tank_capacity = 255
counter_filled_liters = 0
for current_number_line in range(1, number_lines + 1):
    liters = int(input())

    if tank_capacity - liters < 0:
        print("Insufficient capacity!")
        continue
    tank_capacity -= liters
    counter_filled_liters += liters

print(f"{counter_filled_liters}")

