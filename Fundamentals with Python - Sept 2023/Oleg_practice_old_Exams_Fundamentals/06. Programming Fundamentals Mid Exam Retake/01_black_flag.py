plunder_days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_plunder = 0

for current_day in range(1, plunder_days + 1):
    total_plunder += daily_plunder

    if current_day % 3 == 0:
        total_plunder += daily_plunder / 2

    if current_day % 5 == 0:
        total_plunder -= total_plunder * 0.3

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")

else:
    print(f"Collected only {total_plunder / expected_plunder * 100:.2f}% of the plunder.")