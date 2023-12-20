divisor = int(input())
boundary = int(input())
max_number = 0
for n in range(1, boundary + 1):

    if n % divisor == 0 and n <= boundary and n > 0:
       if n > max_number:
            max_number = n

print(max_number)

