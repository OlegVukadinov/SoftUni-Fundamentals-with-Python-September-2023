targets_list = [int(x) for x in input().split("|")]
points = 0

while True:
    command = input().split("@")
    if command[0] == "Game over":
        break

    if command[0] == "Shoot Left":
        start_index, length = int(command[1]), int(command[2])
        if 0 <= start_index < len(targets_list):
            index = (start_index - length) % len(targets_list)
            if index < 0:
                index += len(targets_list)
            target = targets_list[index]
            if target >= 5:
                targets_list[index] -= 5
                points += 5
            else:
                points = target
                targets_list[index] = 0
    elif command[0] == "Shoot Right":
        start_index, length = int(command[1]), int(command[2])
        if 0 <= start_index < len(targets_list):
            index = (start_index + length) % len(targets_list)
            target = targets_list[index]
            if target >= 5:
                targets_list[index] -= 5
                points += 5
            else:
                points = target
                targets_list[index] = 0
    elif command[0] == "Reverse":
        targets_list.reverse()

print(" - ".join(map(str, targets_list)))
print(f"John finished the archery tournament with {points} points!")
