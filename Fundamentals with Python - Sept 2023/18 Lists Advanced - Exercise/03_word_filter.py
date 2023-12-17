text_list = input().split()
new_text_list = [s for s in text_list if len(s) % 2 == 0]

for word in new_text_list:

    print("".join(word))