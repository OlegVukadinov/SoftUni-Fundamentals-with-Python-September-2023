my_list = list(map(int, input().split()))
sorted_my_list = []

average_num = sum(my_list) / len(my_list)

for el in my_list:
    if el > average_num:
        sorted_my_list.append(el)

sorted_my_list.sort(reverse=True)
if len(sorted_my_list) == 0:
    print("No")
else:
    print(*sorted_my_list[:5])