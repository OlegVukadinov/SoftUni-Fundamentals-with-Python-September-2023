def is_valid(some_password):

    if len(some_password) < 6 or len(some_password) > 10:
        print("Password must be between 6 and 10 characters")
    if not some_password.isalnum():
        print("Password must consist only of letters and digits")
    counter_digit = 0
    for x in some_password:
        if x.isdigit():
            counter_digit += 1
    if counter_digit < 2:
        print("Password must have at least 2 digits")
    else:
        print("Password is valid")


entered_pass = input()

is_valid(entered_pass)
