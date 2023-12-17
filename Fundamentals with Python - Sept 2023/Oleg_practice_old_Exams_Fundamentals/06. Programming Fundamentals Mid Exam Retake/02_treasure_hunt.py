initial_loot = input().split("|")
command = input()
while command != "Yohoho!":
    tokens = command.split()
    action = tokens[0]

    if action == "Loot":
        items_to_add = tokens[1:]
        for item in items_to_add:
            if item not in initial_loot:
                initial_loot.insert(0, item)

    elif action == "Drop":
        index = int(tokens[1])
        if 0 <= index < len(initial_loot):
            removed_item = initial_loot.pop(index)
            initial_loot.append(removed_item)

    elif action == "Steal":
        count = int(tokens[1])
        if count >= len(initial_loot):
            stolen_items = initial_loot
            initial_loot = []
        else:
            stolen_items = initial_loot[-count:]
            initial_loot = initial_loot[:-count]

        print(", ".join(stolen_items))

    command = input()

if initial_loot:
    average_gain = sum(len(item) for item in initial_loot) / len(initial_loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")