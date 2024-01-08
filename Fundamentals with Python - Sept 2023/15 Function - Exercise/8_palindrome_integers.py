list_numbers = input().split(", ")
number_forward = ""
number_backward = ""
for number in list_numbers:
    number_forward = number
    number_backward = number[::-1]
    if number_forward == number_backward:
        print("True")
    else:
        print("False")

