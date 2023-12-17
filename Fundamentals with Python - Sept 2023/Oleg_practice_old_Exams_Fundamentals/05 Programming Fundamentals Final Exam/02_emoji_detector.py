import re

input_text = input()

pattern = r"([*]{2}|[:]{2})([A-Z]{1}[a-z]{2,})(\1)"
matches = re.findall(pattern, input_text)

cool_threshold = 1
for char in input_text:
    if char.isdigit():
        cool_threshold *= int(char)

cool_emojis = []
for emoji in matches:
    coolnes = 0
    for character in emoji[1]:
        coolnes += ord(character)

    if coolnes > cool_threshold:
        cool_emojis.append(emoji)

print(f"Cool threshold: {cool_threshold}")
if len(matches) > 0:
    print(f"{len(matches)} emojis found in the text. The cool ones are:")
    for emoji in cool_emojis:
        print(f"{''.join(emoji)}")
