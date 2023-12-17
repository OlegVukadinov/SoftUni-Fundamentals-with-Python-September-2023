array_values = list(map(int, input().split()))

while True:
    command = input().split()
    com = command[0]

    if com == "end":
        break

    if com == "swap":
        array_values[int(command[1])], array_values[int(command[2])] = array_values[int(command[2])], array_values[int(command[1])]
    if com == "multiply":
        array_values[int(command[1])] *= array_values[int(command[2])]
    if com == "decrease":
        array_values = [x - 1 for x in array_values]


print(", ".join(str(el) for el in array_values))