strings = input().split()

total_sum = 0

for str in strings:
        #total_sum += calculate_result(s)
    #for ind in range(len(str)):
        char_before = str[0]
        char_after = str[-1]
        num = int(str[1:-1])

            # Calculate based on the rules
        if char_before.isupper():
            total_sum += num / (ord(char_before) - ord('A') + 1)
        else:
            total_sum += num * (ord(char_before) - ord('a') + 1)

        if char_after.isupper():
            total_sum -= (ord(char_after) - ord('A') + 1)
        else:
            total_sum += (ord(char_after) - ord('a') + 1)

print(f"{total_sum:.2f}")

