text = input()
encrypted_text = ""

for character in text:
    encr_char = chr(ord(character) + 3)
    encrypted_text += encr_char

print(encrypted_text)
