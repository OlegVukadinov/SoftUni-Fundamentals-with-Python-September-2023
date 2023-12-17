list_numbers = list(map(int,input().split()))
list_numbers_even = []
for num in list_numbers:
    if num % 2 == 0:
        list_numbers_even.append(num)

print(list_numbers_even)