number = input()
counter_even = 0
counter_odd = 0
for i in number:
    if int(i) % 2 == 0:
        counter_even += int(i)
    else:
        counter_odd += int(i)

print(f"Odd sum = {counter_odd}, Even sum = {counter_even}")