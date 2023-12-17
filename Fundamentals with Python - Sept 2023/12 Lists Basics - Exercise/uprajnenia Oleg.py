import re

def extract_hidden_message(input_string):
    digits = [int(digit) for digit in re.findall(r'\d', input_string)]
    take_list = [digits[i] for i in range(len(digits)) if i % 2 == 0]
    skip_list = [digits[i] for i in range(len(digits)) if i % 2 != 0]

    non_numbers = [char for char in input_string if not char.isdigit()]
    result = []

    while take_list or skip_list:
        take_count = take_list.pop(0)
        skip_count = skip_list.pop(0)

        result += non_numbers[:take_count]
        non_numbers = non_numbers[take_count + skip_count:]

    return ''.join(result)

# Input string
input_string = input()

# Extract and print the hidden message
hidden_message = extract_hidden_message(input_string)
print(hidden_message)
