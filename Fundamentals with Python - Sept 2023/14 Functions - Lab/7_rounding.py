my_list = list(map(float, input().split()))
rounded_list = []
for i in my_list:
    rounded_list.append(round(i))

print(rounded_list)