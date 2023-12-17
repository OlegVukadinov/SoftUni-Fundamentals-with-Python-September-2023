string_list = input().split(", ")

non_zeros_list = []
zeros_list = []

for i in range(len(string_list)):
    string_list[i] = int(string_list[i])

for num in string_list:
    if num == 0:
        zeros_list.append(num)
    else:
        non_zeros_list.append(num)
result =  non_zeros_list + zeros_list

print(result)