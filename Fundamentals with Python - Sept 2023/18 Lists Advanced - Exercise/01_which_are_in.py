sequences1 = input().split(", ")
sequences2 = input().split(", ")

filtered_list = []

for first_str in sequences1:
    for second_str in sequences2:
        if first_str in second_str:
            filtered_list.append(first_str)
            break
print(filtered_list)