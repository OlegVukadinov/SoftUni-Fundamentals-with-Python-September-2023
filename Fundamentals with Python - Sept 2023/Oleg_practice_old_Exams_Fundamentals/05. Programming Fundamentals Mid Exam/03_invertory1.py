items_list = input().split(", ")

while True:
    command_data = input()
    if command_data == "Craft!":
        break

    command, item = command_data.split(" - ")
    # action = command[0]
    # item = command[1]

    if command == "Collect":
        if item not in items_list:
            items_list.append(item)

    elif command == "Drop":
        if item in items_list:
            items_list.remove(item)

    elif command == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in items_list:
            old_item_index = items_list.index(old_item)
            items_list.insert(old_item_index + 1, new_item)
        # else:
        #     continue

    elif command == "Renew":
        if item in items_list:
            items_list.remove(item)
            items_list.append(item)

print(", ".join(items_list))
