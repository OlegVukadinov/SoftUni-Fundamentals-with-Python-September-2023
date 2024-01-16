my_string = ""

while True:
    command = input().split()
    action = command[0]

    if action == "End":
        break

    if action == "Add":
        sub_string = command[1]
        my_string += sub_string

    elif action == "Upgrade":
        char = command[1]
        new_text = ""
        for c in my_string:
            if c == char:
                new_text += chr(ord(c) + 1)
            else:
                new_text += c
        my_string = new_text

    elif action == "Print":
        print(my_string)

    elif action == "Index":
        char = command[1]
        indexes = [str(i) for i, c in enumerate(my_string) if c == char]
        if indexes:
            print(" ".join(indexes))
        else:
            print("None")

    elif action == "Remove":
        sub_string = command[1]
        my_string = my_string.replace(sub_string, "")