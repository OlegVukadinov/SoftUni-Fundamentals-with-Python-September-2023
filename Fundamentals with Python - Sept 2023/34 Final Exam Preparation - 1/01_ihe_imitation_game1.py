message = input()

while True:
    command = input()
    if command == "Decode":
        break
    instructions = command.split("|")
    action = instructions[0]

    if action == "Move":
        number_of_letters = int(instructions[1])
        message = message[number_of_letters:] + message[:number_of_letters]

    elif action == "Insert":
        index = int(instructions[1])
        value = instructions[2]
        message = message[:index] + value + message[index:]

    elif action == "ChangeAll":
        substring = instructions[1]
        replacement = instructions[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")
