days = int(input())
budget = float(input())
people = int(input())
fuel_price_per_km = float(input())
food_expenses_per_person_per_day = float(input())
hotel_price_per_night_per_person = float(input())

accommodation_expenses = people * days * hotel_price_per_night_per_person
if people > 10:
    accommodation_expenses *= 0.75

food_expenses = people * days * food_expenses_per_person_per_day
total_expenses = accommodation_expenses + food_expenses
for day in range(1, days + 1):
    distance = float(input())
    travel_expenses = distance * fuel_price_per_km
    total_expenses += travel_expenses

    if day % 3 == 0:
        total_expenses *= 1.4
    elif day % 5 == 0:
        total_expenses *= 1.4
    elif day % 7 == 0:
        total_expenses -= total_expenses / people

    if total_expenses > budget:
        needed_money = total_expenses - budget
        print(f"Not enough money to continue the trip. You need {needed_money:.2f}$ more.")
        break

if total_expenses <= budget:
    remaining_budget = budget - total_expenses
    print(f"You have reached the destination. You have {remaining_budget:.2f}$ budget left.")
