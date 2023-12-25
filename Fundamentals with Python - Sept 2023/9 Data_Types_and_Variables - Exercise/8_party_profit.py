group_size = int(input())
days = int(input())
companions_count = group_size
coins = 0

for current_day in range(1, days + 1):

    if current_day % 10 == 0:
        companions_count -= 2

    if current_day % 15 == 0:
        companions_count += 5

    if current_day % 3 == 0:
        coins -= 3 * companions_count
    if current_day % 5 == 0:
        coins += 20 * companions_count
    if current_day % 5 == 0 and current_day % 3 == 0:
        coins -= 2 * companions_count

    coins += 50
    coins -= 2 * companions_count

money_per_companion = int(coins / companions_count)

print(f"{companions_count} companions received {money_per_companion} coins each.")