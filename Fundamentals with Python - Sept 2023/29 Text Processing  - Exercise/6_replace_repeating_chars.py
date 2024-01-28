text = input()
final_text = ""
last_added_char = ""
for letter in text:
    if letter != last_added_char:
        last_added_char = letter
        final_text += letter

print(final_text)


