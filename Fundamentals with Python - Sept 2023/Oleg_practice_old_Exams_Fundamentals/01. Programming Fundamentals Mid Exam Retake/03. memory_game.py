sequence = input().split()
moves = 0

while True:
    command = input()
    if command == "end":
        break

    moves += 1
    index1, index2 = map(int, command.split())

    if index1 == index2 or index1 < 0 or index2 < 0 or index1 >= len(sequence) or index2 >= len(sequence):
        print("Invalid input! Adding additional elements to the board")
        middle_index = len(sequence) // 2
        sequence.insert(middle_index, f"-{moves}a")
        sequence.insert(middle_index, f"-{moves}a")
        continue

    if sequence[index1] == sequence[index2]:
        element = sequence[index1]
        sequence = [x for i, x in enumerate(sequence) if i != index1 and i != index2]
        print(f"Congrats! You have found matching elements - {element}!")
    else:
        print('Try again!')

    if len(sequence) == 0 or len(sequence) == 1:
        break

if len(sequence) > 1:
    print("Sorry you lose :(")
    print(" ".join(sequence))
else:
    print(f"You have won in {moves} turns!")
