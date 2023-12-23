n = int(input())
searched_word = input()

my_list = []
filtered_list = []
for _ in range(n):
    strings = input()
    my_list.append(strings)

    if searched_word in strings:
        filtered_list.append(strings)

print(my_list)
print(filtered_list)