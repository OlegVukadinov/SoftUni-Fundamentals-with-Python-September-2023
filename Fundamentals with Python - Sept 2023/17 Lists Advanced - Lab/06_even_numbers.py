my_list = list(map(int, input().split(", ")))
filtered_list = map(lambda x: x if my_list[x] % 2 == 0 else 'no', range(len(my_list)))
final_list = list(filter(lambda a: a != 'no', filtered_list))
print(final_list)