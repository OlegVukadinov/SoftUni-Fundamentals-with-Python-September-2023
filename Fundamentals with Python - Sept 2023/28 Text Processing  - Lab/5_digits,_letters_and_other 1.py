text = input()
numbers = " "
letters = " "
signs = " "
for element in text:
    if element.isdigit():
        numbers += element
    elif element.isalpha():
        letters += element
    else:
        signs += element

print(numbers)
print(letters)
print(signs)