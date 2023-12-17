key = int(input())
number_lines = int(input())

for current_number_lines in range(number_lines):
    letter = input()

    letter_as_number = ord(letter) + key
    letter_as_letter = chr(letter_as_number)

    print(letter_as_letter, end="")
