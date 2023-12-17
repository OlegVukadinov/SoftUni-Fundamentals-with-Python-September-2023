list_to_do_notes = [0] * 10

while True:
    command = input().split("-")
    if command[0] == "End":
        break

    importance = int(command[0]) - 1
    note = command[1]
    list_to_do_notes.pop(importance)
    list_to_do_notes.insert(importance, note)
final_list = [s for s in list_to_do_notes if s != 0]
print(final_list)