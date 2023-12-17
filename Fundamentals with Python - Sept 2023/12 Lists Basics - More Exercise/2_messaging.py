sequence_of_numbers = input().split()
message = input()
my_list = []
for curr_number in sequence_of_numbers:
    curr_sum = 0
    for i in curr_number:
        curr_sum += int(i)

    curr_sum %= len(message)

    my_list.append(message[curr_sum])
    message = message.replace(message[curr_sum], "", 1)

print(''.join(my_list))

