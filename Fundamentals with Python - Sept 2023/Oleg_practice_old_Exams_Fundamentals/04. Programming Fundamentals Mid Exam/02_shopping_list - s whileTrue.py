product_list = input().split("!")

while True:
    command = input()

    if command == "Go Shopping!":
        break
    tokens = command.split()
    action = tokens[0]

    if action == "Urgent":
        item = tokens[1]
        if item not in product_list:
            product_list.insert(0, item)

    elif action == "Unnecessary":
        item = tokens[1]
        if item in product_list:
            product_list.remove(item)

    elif action == "Correct":
        old_item = tokens[1]
        new_item = tokens[2]
        if old_item in product_list:
            index = product_list.index(old_item)
            product_list[index] = new_item

    elif action == "Rearrange":
        item = tokens[1]
        if item in product_list:
            product_list.remove(item)
            product_list.append(item)

print(", ".join(product_list))
