number_lines = int(input())
counter_left_bracket = 0
counter_right_bracket = 0
for current_number_lines in range(1, number_lines + 1):
    string = input()

    if string == "(":
        counter_left_bracket += 1

    if string == ")":
        counter_right_bracket += 1

if counter_left_bracket == counter_right_bracket:
    print("BALANCED")
else:
    print("UNBALANCED")

# Jydge 75/100
