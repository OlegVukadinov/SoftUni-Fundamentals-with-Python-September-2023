initial_string = input()

numbers_list = []
non_numbers_list = []

take_list = []
skip_list = []

for i in initial_string:
    if i.isdigit():
        numbers_list.append(i)
    else:
        non_numbers_list.append(i)

# for cur_index in range(0, len(numbers_list)):
#     if cur_index % 2 == 0:
#         for el in numbers_list:
#             take_list.append(str(el(cur_index)))
#     else:
#         skip_list.append(cur_index)

take_list = [s[i] for i in range(len(numbers_list)) if i % 2 == 0]
skip_list = [s[i] for i in range(len(numbers_list)) if i % 2 != 0]


print(take_list)
print(skip_list)
