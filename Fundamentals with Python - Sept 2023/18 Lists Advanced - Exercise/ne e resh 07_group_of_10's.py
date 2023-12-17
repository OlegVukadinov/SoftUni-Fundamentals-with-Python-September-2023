sequence_of_numbers = list(map(int, input().split(", ")))
list_till_10 = []
list_till_20 = []
list_till_30 = []
list_till_40 = []
list_till_50 = []

for number in sequence_of_numbers:
    if number <= 10:
        list_till_10.append(number)
        #sequence_of_numbers.remove(number)
    elif 11 <= number <= 20:
        list_till_20.append(number)
        #sequence_of_numbers.remove(number)
    elif 21 <= number <= 30:
        list_till_30.append(number)
        #sequence_of_numbers.remove(number)
    elif 31 <= number <= 40:
        list_till_40.append(number)
        #sequence_of_numbers.remove(number)
    elif 41 <= number <= 50:
        list_till_50.append(number)

        #sequence_of_numbers.remove(number)


print(f"Group of {10}'s: {list_till_10}")
print(f"Group of {20}'s: {list_till_20}")
print(f"Group of {30}'s: {list_till_30}")
print(f"Group of {40}'s: {list_till_40}")
print(f"Group of {50}'s: {list_till_50}")
