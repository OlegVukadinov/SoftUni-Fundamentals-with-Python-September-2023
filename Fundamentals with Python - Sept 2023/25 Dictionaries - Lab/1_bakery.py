food_info = input().split()

food_dict = {}

for i in range(0, len(food_info), 2):
    food = food_info[i]
    quantity = food_info[i + 1]
    food_dict[food] = int(quantity)

print(food_dict)

