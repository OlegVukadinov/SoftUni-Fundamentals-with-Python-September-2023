elements_list = input().split()

count_moves = 0

while True:
    command = input()

    if command == "end":
        break

    count_moves += 1

    indexes = command.split()
    ind1 = int(indexes[0])
    ind2 = int(indexes[1])

    if ind1 == ind2 or not (0 <= ind1 < len(elements_list)) or not (0 <= ind2 < len(elements_list)):
        elements_list.insert(len(elements_list) // 2, f"-{count_moves}a")
        elements_list.insert(len(elements_list) // 2, f"-{count_moves}a")
        print("Invalid input! Adding additional elements to the board")
        continue
    if elements_list[ind1] == elements_list[ind2]:
        matching_element = elements_list[ind1]
        elements_list = [x for i, x in enumerate(elements_list) if i != ind1 and i != ind2]
        print(f"Congrats! You have found matching elements - {matching_element}!")
    else:
        print('Try again!')

    if len(elements_list) == 0 or len(elements_list) == 1:
        break

if len(elements_list) > 1:
    print("Sorry you lose :(")
    print(" ".join(elements_list))
else:
    print(f"You have won in {count_moves} turns!")
