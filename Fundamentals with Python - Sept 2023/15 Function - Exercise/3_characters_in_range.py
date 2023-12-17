def characters_in_range(first_char, second_char):
    characters = []
    for curr_char in range(ord(first_char) + 1, ord(second_char)):
        characters.append(chr(curr_char))
    return characters


char1 = input()
char2 = input()

result = characters_in_range(char1, char2)
print(" ".join(result))