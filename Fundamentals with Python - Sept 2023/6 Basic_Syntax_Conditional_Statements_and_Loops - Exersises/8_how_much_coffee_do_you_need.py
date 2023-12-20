needed_cofee = 0

while True:
    command = input()

    if command == "END":
        break

    elif command == "coding" or command == "dog" \
            or command == "cat" or command == "movie":
        needed_cofee += 1
    elif command == "CODING" or command == "DOG" \
            or command == "CAT" or command == "MOVIE":
        needed_cofee += 2
    else:
        continue
if needed_cofee > 5:
    print("You need extra sleep")

else:
    print(f"{needed_cofee}")
