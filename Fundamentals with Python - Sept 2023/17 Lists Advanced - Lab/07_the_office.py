employees_happiness = list(map(int,input().split()))
happy_factor = int(input())

employees_happiness = [s * happy_factor for s in employees_happiness]
average_happiness = sum(employees_happiness)/ len(employees_happiness)
filtered_employees_happiness = [s for s in employees_happiness if s > average_happiness]
if len(filtered_employees_happiness) >= len(employees_happiness) / 2:
    print(f"Score: {len(filtered_employees_happiness)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_employees_happiness)}/{len(employees_happiness)}. Employees are not happy!")
