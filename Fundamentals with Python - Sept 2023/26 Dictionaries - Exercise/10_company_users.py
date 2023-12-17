company_data = {}

while True:
    command = input()

    if command == "End":
        break

    company_name, employee_id = command.split(" -> ")

    if company_name not in company_data:
        company_data[company_name] = []
    if employee_id not in company_data[company_name]:
        company_data[company_name].append(employee_id)

    # filtered_data = {company_name for name, employee_id in company_data.items() if }
    for curr_employee_id in range(len(company_data.values())):
        if curr_employee_id in company_data.values():
            del company_data[employee_id]

for name, id in company_data.items():
    print(f"{name}")
    for curr_id in id:
        print(f"-- {curr_id}")

