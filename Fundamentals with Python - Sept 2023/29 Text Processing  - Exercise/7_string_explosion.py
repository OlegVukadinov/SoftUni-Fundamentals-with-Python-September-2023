some_string = input()
final_string = ""
strenght = 0

for index in range(len(some_string)):
    if strenght > 0 and some_string[index] != ">":
        strenght -= 1
    elif some_string[index] == ">":
        final_string += some_string[index]
        strenght += int(some_string[index + 1])
    else:
        final_string += some_string[index]

print(final_string)

