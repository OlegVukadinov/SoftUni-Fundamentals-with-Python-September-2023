init_string = input()

while True:
    command = input()
    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {init_string}")
        break

    com = command.split(":")
    action = com[0]

    if action == "Add Stop":
        index = int(com[1])
        string = com[2]
        if 0 <= index < len(init_string):
            init_string = init_string[:index] + string + init_string[index:]
        print(init_string)

    elif action == "Remove Stop":
        start_index = int(com[1])
        end_index  = int(com[2])
        if 0 <= start_index < len(init_string) and 0 <= end_index < len(init_string):
            init_string = init_string[:start_index] + init_string[end_index + 1:]
        print(init_string)

    elif action == "Switch":
        old_string = com[1]
        new_string = com[2]
        if old_string in init_string:
            init_string = init_string.replace(old_string,new_string)
        print(init_string)
