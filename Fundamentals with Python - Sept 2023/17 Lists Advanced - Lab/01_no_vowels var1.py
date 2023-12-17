text = input()
filtered_text = [letter for letter in text if letter not in ['a', 'o', 'u', 'e', 'i','A', 'O', 'U', 'E', 'I']]
print("".join(filtered_text))