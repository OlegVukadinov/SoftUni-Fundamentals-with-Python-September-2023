number_list = list(map(int, input().split(", ")))
new_list = []

for el in number_list:
    if el % 2 == 0:
        new_list.append(number_list.index(el))

print(new_list)