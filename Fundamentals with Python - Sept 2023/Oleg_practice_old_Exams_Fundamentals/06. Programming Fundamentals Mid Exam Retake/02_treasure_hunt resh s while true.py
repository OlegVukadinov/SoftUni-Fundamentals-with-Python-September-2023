items_list = input().split("|")

while True:
    command_data = input()
    if command_data == "Yohoho!":
        break

    com = command_data.split()
    command = com[0]

    if command == "Loot":
        items = com[1:]
        for curr_item in items:
            if curr_item not in items_list:
                items_list.insert(0,curr_item)

    if command == "Drop":
        index = int(com[1])
        if 0 <= index < len(items_list):# проверка дали индекса е валиден
            removed_item = items_list.pop(index)
            items_list.append(removed_item)

    if command == "Steal":
        count = int(com[1])
        if count >= len(items_list):
            stolen_items = items_list
            items_list = []
        else:
            stolen_items = items_list[-count:]
            items_list = items_list[:-count]

        print(", ".join(stolen_items))

if items_list:
    average_gain = sum(len(item) for item in items_list) / len(items_list)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
