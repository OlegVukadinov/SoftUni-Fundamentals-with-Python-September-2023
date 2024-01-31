init_string = input()
while True:
    command = input()
    if command == "Done":
        break

    com = command.split(' ')
    action = com[0]

    if action == "TakeOdd":
        init_string = init_string[1::2]
        print(init_string)

    elif action == "Cut":
        index = int(com[1])
        lenght = int(com[2])
        init_string = init_string[:index] + init_string[index + lenght:]
        print(init_string)

    elif action == "Substitute":
        substring = com[1]
        substitute = com[2]
        if substring in init_string:
            init_string = init_string.replace(substring, substitute)
            print(init_string)
        else:
            print("Nothing to replace!")

print(f"Your password is: {init_string}")