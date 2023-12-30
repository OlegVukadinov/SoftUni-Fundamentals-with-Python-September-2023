def pass_validator(pass_word):
    valid_counter = 0
    
    if len(pass_word) < 6 or len(pass_word) > 10:
        print("Password must be between 6 and 10 characters")
    else:
        valid_counter += 1

    if not pass_word.isalnum():
        print("Password must consist only of letters and digits")
    else:
        valid_counter += 1

    digit_counter = 0
    for el in pass_word:
        if el.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
    else:
        valid_counter += 1

    if valid_counter == 3:
        print("Password is valid")


password = input()
pass_validator(password)