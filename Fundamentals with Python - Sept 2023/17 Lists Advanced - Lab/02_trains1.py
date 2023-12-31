number_wagons = int(input())
train_list = [0] * number_wagons

while True:
    command = input()
    if command == "End":
        print(train_list)
        break

    com = command.split(" ")
    action = com[0]

    if action == "add":
        people = int(com[1])
        train_list[-1] += people

    elif action == "insert":
        index = int(com[1])
        people = int(com[2])
        train_list[index] += people

    elif action == "leave":
        index = int(com[1])
        people = int(com[2])
        train_list[index] -= people