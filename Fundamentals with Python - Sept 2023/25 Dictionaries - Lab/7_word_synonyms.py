n_words = int(input())

my_dict = {}

for curr_n in range(n_words):
    word = input()
    synonym = input()
    if word not in my_dict:
        my_dict[word] = []
        my_dict[word].append(synonym)
    else:
        my_dict[word].append(synonym)

for word in my_dict:
    print(f"{word} - {', '.join(my_dict[word])}")




