n = int(input())

for current_n in range(1, n + 1):
    current_n_as_string = str(current_n)
    counter = 0
    for i in current_n_as_string:
        counter += int(i)
    if counter == 5 or counter == 7 or counter == 11:
        print(f"{current_n} -> True")
    else:
        print(f"{current_n} -> False")