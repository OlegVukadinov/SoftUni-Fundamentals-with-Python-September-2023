import re

text_string = input()

regex = r'(#|\|)([A-Za-z\s]+)\1(\d{2,2}/\d{2,2}/\d{2,2})\1(\d{1,5})\1'
matches = re.finditer(regex, text_string)
new_list = []
sum_calories = 0
for match in matches:
    new_list.append([match.group(2), match.group(3), match.group(4)])
    sum_calories += int(match.group(4))
days = sum_calories // 2000
print(f"You have food to last you for: {days} days!")
for match in new_list:
    print(f"Item: {match[0]}, Best before: {match[1]}, Nutrition: {match[2]}")
