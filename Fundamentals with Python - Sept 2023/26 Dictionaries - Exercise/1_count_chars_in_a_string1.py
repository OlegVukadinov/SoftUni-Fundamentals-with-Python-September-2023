text = input()
my_dict = {}

for letter in text:
    if letter != " ":
        if letter not in my_dict:
            my_dict[letter] = 1
        else:
            my_dict[letter] += 1
for letter,v in my_dict.items():
    print(f"{letter} -> {my_dict[letter]}")
