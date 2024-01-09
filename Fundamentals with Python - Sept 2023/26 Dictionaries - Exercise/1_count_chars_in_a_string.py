symbols = [character for character in input() if character != " "]
letters = {}

for symbol in symbols:
    if symbol not in letters.keys():
        letters[symbol] = 0
    letters[symbol] += 1
for symbol, occurrences in letters.items():
    print(f"{symbol} -> {occurrences}")


# my_list = input().split()
# repetition = []
#
# for i in my_list:
#     for x in str(i):
#         repetition.append(x)
#         if x in str(i):
#             rep = repetition.count(x)
#
#     print(f"{x} -> {rep}")