concealed_message = input()

while True:
    command = input()

    if command == "Reveal":
        break

    com = command.split(":|:")
    action = com[0]

    if action == "InsertSpace":
        index = int(com[1])
        concealed_message = concealed_message[:index] + ' ' + concealed_message[index:]
        print(concealed_message)

    elif action == "Reverse":
        substring = com[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, '', 1)
            concealed_message += substring[::-1]
            print(concealed_message)
        else:
            print("error")

    elif action == "ChangeAll":
        substring = com[1]
        replacement = com[2]

        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)

print(f"You have a new text message: {concealed_message}")