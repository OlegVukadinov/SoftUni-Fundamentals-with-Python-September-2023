card_list = input().split(", ")
n = int(input())

for curr_n in range(1, n + 1):

    command = input().split(", ")
    action = command[0]

    if action == "Add":
        card_name = command[1]
        if card_name in card_list:
            print("Card is already in the deck")
        else:
            card_list.append(card_name)
            print("Card successfully added")

    elif action == "Remove":
        card_name = command[1]
        if card_name in card_list:
            card_list.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")

    elif action == "Remove At":
        index = int(command[1])

        if 0 <= index < len(card_list):
            card_list.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")

    elif action == "Insert":
        index = int(command[1])
        card_name = command[2]
        if 0 <= index < len(card_list):
            continue

        else:
            print("Index out of range")

        if card_name not in card_list and 0 <= index < len(card_list):
            card_list.insert(index, card_name)
            print("Card successfully added")

        elif card_name in card_list:
            print("Card is already added")

print(", ".join(card_list))