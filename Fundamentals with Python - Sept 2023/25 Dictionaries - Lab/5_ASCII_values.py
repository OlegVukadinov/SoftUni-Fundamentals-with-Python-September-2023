char_list = input().split(", ")

my_dict = {}

for i in range(len(char_list)):
    key = char_list[i]
    value = ord(char_list[i])
    my_dict[key] = int(value)

print(my_dict)