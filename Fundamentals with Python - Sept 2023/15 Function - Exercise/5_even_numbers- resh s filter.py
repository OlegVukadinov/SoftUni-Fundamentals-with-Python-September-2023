list_numbers = list(map(int,input().split()))
result = filter(lambda x: x % 2 == 0, list_numbers)

print(list(result))