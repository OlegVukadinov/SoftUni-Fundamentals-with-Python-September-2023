num_cities = int(input())

curr_profit = 0
total_profit = 0
counter_curr_profit = 0
for curr_num_city in range(1, num_cities + 1):
    city_name = input()
    income_money = float(input())
    expenses = float(input())

    if curr_num_city % 5 == 0:
        income_money -= income_money * 0.10
    elif curr_num_city % 3 == 0:
        expenses += expenses / 2

    curr_profit = income_money - expenses
    counter_curr_profit += curr_profit
    print(f"In {city_name} Burger Bus earned {curr_profit:.2f} leva.")

print(f"Burger Bus total profit: {counter_curr_profit:.2f} leva.")