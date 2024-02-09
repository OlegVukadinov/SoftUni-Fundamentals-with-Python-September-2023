sequence_list = list(map(int, input().split()))

average_number = sum(sequence_list) / len(sequence_list)
sequence_list.sort(reverse=True)
new_list = []

for curr_num in sequence_list:
    if curr_num > average_number:
        new_list.append(curr_num)

if len(new_list) == 0:
    print("No")
else:
    print(" ".join(map(str, new_list[:5])))
