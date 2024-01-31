food_kg = float(input())
hay_kg = float(input())
cover_kg = float(input())
pig_weight_kg = float(input())

food_gr = food_kg * 1000
hay_gr = hay_kg * 1000
cover_gr = cover_kg * 1000
pig_weight_gr = pig_weight_kg * 1000
days = 30

for current_day in range(1, days + 1):
    food_gr -= 300

    if current_day % 2 == 0:
        hay_gr -= food_gr * 0.05

    if current_day % 3 == 0:
        cover_gr -= 1 / 3 * pig_weight_gr

if food_gr <= 0 or hay_gr <= 0 or cover_gr <= 0:
    print("Merry must go to the pet store!")

elif food_gr > 0 or hay_gr > 0 or cover_gr > 0:
    print(f"Everything is fine! Puppy is happy! Food: {food_gr / 1000:.2f}, Hay: {hay_gr / 1000:.2f}, Cover: {cover_gr / 1000:.2f}.")
