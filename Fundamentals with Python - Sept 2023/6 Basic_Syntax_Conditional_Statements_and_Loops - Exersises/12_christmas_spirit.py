quantity_of_decorations = int(input())
days_till_christmas = int(input())

counter_price = 0
counter_spirit = 0
price_ornament_set = 2
price_tree_skirt = 5
price_tree_garland = 3
price_tree_lights = 15

for current_day in range(1, days_till_christmas + 1):

    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        counter_price += price_ornament_set * quantity_of_decorations
        counter_spirit += 5
    if current_day % 3 == 0:
        counter_price += price_tree_skirt * quantity_of_decorations + price_tree_garland * quantity_of_decorations
        counter_spirit += 3 + 10
    if current_day % 5 == 0:
        counter_price += price_tree_lights * quantity_of_decorations
        counter_spirit += 17
        if current_day % 3 == 0:
            counter_spirit += 30
    if current_day % 10 == 0:
        counter_spirit -= 20
        counter_price += price_tree_skirt + price_tree_garland + price_tree_lights

if days_till_christmas % 10 == 0:
    counter_spirit -= 30

print(f"Total cost: {counter_price}")
print(f"Total spirit: {counter_spirit}")
