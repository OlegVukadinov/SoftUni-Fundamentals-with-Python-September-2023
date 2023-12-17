sequence = input().split()
new_sequence = []

for curr_seq in sequence:
    new_sequence.append(curr_seq * len(curr_seq))

print(''.join(new_sequence))