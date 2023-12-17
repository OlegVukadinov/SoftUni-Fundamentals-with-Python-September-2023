names_of_gifts = input().split()

while True:
    command = input().split(' ')
    if command[0] == "No" or command[1] == "Money":
        break

    if "OutOfStock" in command:
        for i in range(len(names_of_gifts)):
            if command[1] in names_of_gifts[i]:
                names_of_gifts[i] = "None"

    elif "Required" in command:
        for i in range(len(names_of_gifts)):
            if i == int(command[2]):
                names_of_gifts[i] = command[1]
    elif "JustInCase" in command:
        names_of_gifts[-1] = command[1]
while "None" in names_of_gifts:
    names_of_gifts.remove("None")
for i in names_of_gifts:
    print(i, end=" ")