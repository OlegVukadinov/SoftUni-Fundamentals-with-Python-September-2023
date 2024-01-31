numbers = [int(el) for el in input().split()]

command = input().split()

while not command == 'end':
    com = command[0]
    if com == 'end':
        break
    if com == 'swap':
        numbers[int(command[1])], numbers[int(command[2])] = numbers[int(command[2])], numbers[int(command[1])]
    elif com == 'multiply':
        numbers[int(command[1])] *= numbers[int(command[2])]
    if com == 'decrease':
        numbers = [x - 1 for x in numbers]

    command = input().split()

print(', '.join(str(el) for el in numbers))
