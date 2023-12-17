fire_cells = input().split("#")
water = int(input())

effort = 0
total_fire = []

for i in range(len(fire_cells)):
    level, cell = fire_cells[i].split(" = ")
    cell = int(cell)

    if water < cell:
        break
    if level == "Low" and 1 <= cell <= 50:
        water -= cell
        effort += cell * 0.25
        total_fire.append(cell)
    if level == "Medium" and 51 <= cell <= 80:
        water -= cell
        effort += cell * 0.25
        total_fire.append(cell)
    if level == "High" and 81 <= cell <= 125:
        water -= cell
        effort += cell * 0.25
        total_fire.append(cell)

print("Cells:")
for el in total_fire:
    print(f" - {el}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {str(sum(total_fire))}")
