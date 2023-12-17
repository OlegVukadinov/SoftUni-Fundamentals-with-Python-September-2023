num_messages = int(input())

for current_num_message in range (1, num_messages + 1):
    number = int(input())

    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number > 88:
        print("Bye.")
    elif number != 86 or number != 88 and number < 88:
        print("GREAT!")
