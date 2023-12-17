initial_list = input().split("!")

while True:
    command_data = input()

    if command_data == "Go Shopping!":
        break
    command = command_data.split()
    action = command[0]

    if action == "Urgent":
        item = command [1]
        if item not in initial_list:
            initial_list.insert(0, item)

    elif action == "Unnecessary":
        item = command[1]
        if item in initial_list:
            initial_list.remove(item)

    elif action == "Correct":
        old_item = command[1]
        new_item = command[2]
        if old_item in initial_list:
            index = initial_list.index(old_item)
            initial_list[index] = new_item

    elif action == "Rearrange":
        item = command[1]
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)

print(", ".join(initial_list))


