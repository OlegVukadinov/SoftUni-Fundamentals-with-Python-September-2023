n = int(input())

collection = {}

for _ in range(n):
    info = input().split("|")
    piece, composer, key = info[0], info[1], info[2]
    collection[piece] = {"composer": composer, "key": key}

while True:
    command = input()
    if command == "Stop":
        break

    command_parts = command.split("|")
    action = command_parts[0]
    piece = command_parts[1]

    if action == "Add":
        composer, key = command_parts[2], command_parts[3]

        if piece not in collection:
            collection[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    if action == "Remove":
        if piece in collection:
            del collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    if action == "ChangeKey":
        new_key = command_parts[2]
        if piece in collection:
            collection[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, info in collection.items():
    print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")
