gifts = input().split(" ")

while True:
    command = input().split(" ")
    action = command[0]
    if action == "No" or action == "Money":
        break

    if action == "OutOfStock":
        gift = command[1]
        for i in range(len(gifts)):
            if gift in gifts[i]:
                gifts[i] = "None"

    elif action == "Required":
        gift = command[1]
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif action == "JustInCase":
        gift = command[1]
        gifts.pop()
        gifts.append(gift)

while "None" in gifts:
    gifts.remove("None")

print(" ".join(gifts))