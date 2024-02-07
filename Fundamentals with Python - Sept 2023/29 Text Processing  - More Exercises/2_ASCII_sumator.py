char1 = input()
char2 = input()
random_string = input()

    # Get ASCII codes of the given characters
char1_code = ord(char1)
char2_code = ord(char2)

    # Ensure char1_code is smaller than char2_code
if char1_code > char2_code:
    char1_code, char2_code = char2_code, char1_code

    # Sum ASCII values of characters between char1 and char2 in the input string
total_ascii_sum = sum(ord(char) for char in random_string if char1_code < ord(char) < char2_code)

print(total_ascii_sum)

