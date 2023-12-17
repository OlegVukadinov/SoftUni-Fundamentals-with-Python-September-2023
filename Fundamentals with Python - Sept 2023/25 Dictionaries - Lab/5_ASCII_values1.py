char_list = input().split(", ")

my_dict = {s: ord(s) for s in char_list}

print(my_dict)