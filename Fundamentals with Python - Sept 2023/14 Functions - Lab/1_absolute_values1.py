my_list = list(map(float, input().split()))
new_list = []
for el in my_list:
    el = abs(el)
    new_list.append(el)
print(new_list)