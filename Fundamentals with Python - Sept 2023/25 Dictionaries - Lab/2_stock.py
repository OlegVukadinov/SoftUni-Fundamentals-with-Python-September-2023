food_info = input().split()
food_dict = {}

for i in range(0, len(food_info), 2):
    food = food_info[i]
    quantity = food_info[i + 1]
    food_dict[food] = int(quantity)

searched_product = input().split()

for curr_product in searched_product:
    if curr_product in food_dict:
        print(f"We have {food_dict[curr_product]} of {curr_product} left")
    else:
        print(f"Sorry, we don't have {curr_product}")