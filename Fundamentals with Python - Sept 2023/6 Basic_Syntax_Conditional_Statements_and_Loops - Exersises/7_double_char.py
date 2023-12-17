
while True:
    string = input()
    new_string = ''
    if string == "End":
        break

    if string == "SoftUni":
        continue
    else:
        for letter in string:
            new_string += letter * 2

    print(new_string)