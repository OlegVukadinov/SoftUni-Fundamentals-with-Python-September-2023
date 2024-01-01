words_list = input().split(" ")
palind_text = input()

palindrome_list = []
counter = 0
for el in words_list:
    if el == el[::-1]:
       palindrome_list.append(el)
for el in words_list:
    if palind_text in words_list:
        counter += 1
        words_list.remove(palind_text)


print(palindrome_list)
print(f"Found palindrome {counter} times")