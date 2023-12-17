num_vagons = int(input())
train = [0] * num_vagons

while True:
    command = input()
    if command == "End":
        break

    com = command.split(" ")
    if com[0] == "add":
        train[2] = int(com[1])
    if com[0] == "insert":
        train[0] = int(com[2])

    if com[0] == "leave":
        #train.pop(0, int(com[2]))
        train[0] -= int(com[2])
print(train)