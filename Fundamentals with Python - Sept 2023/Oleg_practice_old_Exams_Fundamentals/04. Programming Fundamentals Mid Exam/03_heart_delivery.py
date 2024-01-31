houses_list = list(map(int, input().split("@")))

current_index = 0

while True:
    command = input().split()

    if command[0] == "Love!":
        break
    jump_lenght = int(command[1])
    current_index += jump_lenght
    if current_index not in range(len(houses_list)):
        current_index = 0
    if houses_list[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        houses_list[current_index] -= 2
        if houses_list[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")


print(f"Cupid's last position was {current_index}.")

if sum(houses_list) == 0:
        print("Mission was successful.")
else:
    houses = [s for s in houses_list if s != 0]
    print(f"Cupid has failed {len(houses)} places.")
