raw_key = input()

while True:
    command = input()
    if command == "Generate":
        print(f"Your activation key is: {raw_key}")
        break

    instructions = command.split(">>>")
    action = instructions[0]

    if action == "Contains":
        substring = instructions[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")

        else:
            print(f"Substring not found!")

    elif action == "Flip":
        start_index = int(instructions[2])
        end_index = int(instructions[3])
        if instructions[1] == "Lower":
           raw_key = raw_key[:start_index] + raw_key[start_index:end_index].lower() + raw_key[end_index:]

        elif instructions[1] == "Upper":
            raw_key = raw_key[:start_index] + raw_key[start_index:end_index].upper() + raw_key[end_index:]
        print(raw_key)

    elif action == "Slice":
        start_index = int(instructions[1])
        end_index = int(instructions[2])
        raw_key = raw_key[:start_index] + raw_key[end_index:]
        print(raw_key)

