n = int(input())

even_list = []
odd_list = []
negative_list = []
positive_list = []

for curr_n in range(n):
    digits = int(input())

    if digits >= 0:
        positive_list.append(digits)
    if digits < 0:
        negative_list.append(digits)
    if digits % 2 == 0:
        even_list.append(digits)
    else:
        odd_list.append(digits)

command = input()
if command == "even":
    print(even_list)
if command == "odd":
    print(odd_list)
if command == "positive":
    print(positive_list)
if command == "negative":
    print(negative_list)
