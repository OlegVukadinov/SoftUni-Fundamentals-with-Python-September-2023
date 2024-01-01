employees = list(map(int, input().split(" ")))
happyness_factor = int(input())

employees = [s * happyness_factor for s in employees]
average_happyness = sum(employees) / len(employees)
filtered_employees = []

for el in employees:
    if el >= average_happyness:
        filtered_employees.append(el)

if len(filtered_employees) >= len(employees) / 2:
    print(f"Score: {len(filtered_employees)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_employees)}/{len(employees)}. Employees are not happy!")