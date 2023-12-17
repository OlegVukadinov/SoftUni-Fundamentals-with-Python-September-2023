stops_string = input()

while True:
    command_data = input()
    if command_data  == "Travel":
        print (f"Ready for world tour! Planned stops: {stops_string}")
        break

    com = command_data.split(":")
    command = com[0]

    if command == "Add Stop":
        index = int(com[1])
        string = com[2]
        if 0 <= index < len(stops_string):
            stops_string = stops_string[:index] + string + stops_string[index:]
            print(stops_string)

    elif command == "Remove Stop":
        start_index = int(com[1])
        end_index= int(com[2])
        if 0 <= start_index < len(stops_string) and 0 <= end_index < len(stops_string):
            stops_string = stops_string[:start_index] + stops_string[end_index + 1:]
        print(stops_string)

    elif command == "Switch":
        old_string = com[1]
        new_string= com[2]
        if old_string in stops_string:
            stops_string = stops_string.replace(old_string, new_string)
        print(stops_string)