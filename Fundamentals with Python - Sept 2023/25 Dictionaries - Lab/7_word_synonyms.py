n = int(input())

my_dict = {}

for curr_n in range(n):
    word = input()
    synonym = input()
    if word not in my_dict:
        my_dict[word] = []
        my_dict[word].append(synonym)
    else:
        my_dict[word].append(synonym)

for key,value in my_dict.items():
    print(f"{key} - {', '.join(value)}")     # защото в случая value е лист от две думи - двата synonym на word

# Алтернативно:
# for word in my_dict.keys():
#     print(f"{word} - {', '.join(my_dict[word])}")


