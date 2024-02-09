pirate_ship_status = list(map(int, input().split(">")))
war_ship_status = list(map(int, input().split(">")))
max_health = int(input())

lost = False

while True:
    command = input().split()
    action = command[0]

    if action == "Retire":
        break

    if action == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(war_ship_status):
            war_ship_status[index] -= damage
            if war_ship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                lost = True
                break
    elif action == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status):

            for curr_index in range(start_index, end_index + 1):
                pirate_ship_status[curr_index] -= damage

                if pirate_ship_status[curr_index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    lost = True
                    break
            if lost:
                break

    elif action == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(pirate_ship_status):
            if pirate_ship_status[index] + health > max_health:
                health = max_health - pirate_ship_status[index]
            pirate_ship_status[index] += health

    elif action == "Status":
        status = max_health * 0.20
        counter = len([s for s in pirate_ship_status if s < status])
        print(f"{counter} sections need repair.")

if not lost:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(war_ship_status)}")
