my_list = list(map(int, input().split(", ")))

for el in my_list:
    if el == 0:
       my_list.remove(el)
       my_list.append(el)

print(my_list)