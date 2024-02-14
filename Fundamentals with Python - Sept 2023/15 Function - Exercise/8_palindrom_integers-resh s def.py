def is_palindrome(some_number):
    if some_number == some_number[::-1]:
        return True
    else:
        return False

list_numbers = input().split(", ")
for number in list_numbers:
    print(is_palindrome(number))