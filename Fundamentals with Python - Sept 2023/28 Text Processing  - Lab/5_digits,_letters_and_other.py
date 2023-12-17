text = input()
number_list = []
letter_list = []
sign_list = []
for element in text:
    if element.isdigit():
        number_list.append(element)
    elif element.isalpha():
        letter_list.append(element)
    else:
        sign_list.append(element)

print("".join(number_list))
print("".join(letter_list))
print("".join(sign_list))