budget = float(input())
price_1kg_flour = float(input())

price_1pack_eggs = price_1kg_flour * 0.75
price_1l_milk = price_1kg_flour + price_1kg_flour * 0.25
price_for_1loaf = price_1kg_flour + price_1pack_eggs + price_1l_milk / 4

counter_loaves = 0
counter_colored_eggs = 0

while budget > price_for_1loaf:
    counter_loaves += 1
    counter_colored_eggs += 3
    budget -= price_for_1loaf

    if counter_loaves % 3 == 0:
        counter_colored_eggs -= (counter_loaves - 2)

print(f"You made {counter_loaves} loaves of Easter bread! Now you have {counter_colored_eggs} eggs and {budget:.2f}BGN left.")