words_list = input().split()
palindrome = input()

list_palindromes = []

palindrome_counter = words_list.count(palindrome)
for word in words_list:
    if word == word[::-1]:
        list_palindromes.append(word)

print(list_palindromes)
print(f"Found palindrome {palindrome_counter} times")