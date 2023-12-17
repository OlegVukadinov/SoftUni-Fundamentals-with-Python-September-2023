pass_word = input()

commands = input()
while commands != 'Complete':
    token = commands.split(' ')
    command = token[0]

    if command == 'Insert':
        char = token[2]
        num = int(token[1])
        if num < len(pass_word):
            pass_word = pass_word[:num] + char + pass_word[num:]
            print(pass_word)
        else:
            continue

    if command == 'Make':
        command = token[1]
        num = int(token[2])
        if command == 'Upper':
            pass_word = pass_word[:num] + pass_word[num].upper() + pass_word[num + 1:]
            print(pass_word)
        elif command == 'Lower':
            pass_word = pass_word[:num] + pass_word[num].lower() + pass_word[num + 1:]
            print(pass_word)

    elif command == 'Replace':
        char = token[1]
        num = int(token[2])
        if char not in pass_word:
            continue
        else:
            sum = int(ord(char) + num)
            char1 = chr(sum)
            pass_word = pass_word.replace(char, char1)
            print(pass_word)

    elif command == 'Validation':
        if len(pass_word) < 8:
            print('Password must be at least 8 characters long')
        elif pass_word.isalnum() == False and '_' not in pass_word:
            print('Password must consist only of letters, digits and _!"')
        elif not any(x.isupper() for x in pass_word):
            print('Password must consist at least one uppercase letter!')
        elif not any(x.islower() for x in pass_word):
            print('Password must consist at least one lowercase letter!')
        elif not any(x.isdigit() for x in pass_word):
            print('Password must consist at least one digit!')

    commands = input()