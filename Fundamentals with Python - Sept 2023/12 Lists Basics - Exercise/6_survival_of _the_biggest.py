my_list = list(map(int,input().split()))
number = int(input())

for current_number in range(1, number + 1):
    my_list.remove(min(my_list))
for i in range(len(my_list)):
    my_list[i] = str(my_list[i])
print(", ".join (my_list))
