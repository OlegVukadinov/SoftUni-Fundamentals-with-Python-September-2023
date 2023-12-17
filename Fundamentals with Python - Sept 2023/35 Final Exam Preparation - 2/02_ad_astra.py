import re
information = input()

pattern = r"(?i)([#|])([a-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)"
matches = re.findall(pattern, information)
total_calories = sum([int(match[5]) for match in matches])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for match in matches:
    item_name = match[1]
    expiration_date = match[3]
    calories = match[5]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")