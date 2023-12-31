to_do_list = [0] * 10
while True:
    command = input()
    if command == "End":
        break

    com = command.split("-")
    importans = int(com[0])
    note = com[1]

    for importance in com:
        to_do_list.pop(importans - 1)
        to_do_list.insert(importans - 1, note)
new_list = [s for s in to_do_list if s != 0]
print(new_list)