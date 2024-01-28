def lenght_is_valid(some_username):
    if 3 <= len(some_username) <= 16:
        return True
    else:
        return False
def char_are_valid(some_username):
    for character in some_username:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    else:
        return True
def no_reduntant_symbol(some_username):
    if " " in some_username:
        return False
    else:
        return True

def username_is_valid(some_username):
    if lenght_is_valid(some_username) and char_are_valid(some_username) and no_reduntant_symbol(some_username):
        return True
    else:
        return False
usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)


