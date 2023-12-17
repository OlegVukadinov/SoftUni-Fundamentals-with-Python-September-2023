text = input()
for current_index in range(len(text)):
    if text[current_index] == ':':
        print(f":{text[current_index + 1]}")