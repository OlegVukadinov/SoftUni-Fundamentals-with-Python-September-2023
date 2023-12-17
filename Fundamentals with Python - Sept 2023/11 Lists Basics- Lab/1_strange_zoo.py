string1 = input()
string2 = input()
string3 = input()

my_list = []
my_list.append(string1)
my_list.append(string2)
my_list.append(string3)

my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)