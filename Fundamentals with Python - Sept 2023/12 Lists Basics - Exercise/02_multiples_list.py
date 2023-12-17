factor = int(input())
count = int(input())

my_list = []

for curr_count in range(1, count + 1):
    my_list.append(curr_count * factor)

print(my_list)