resourses_dict = {}

while True:
    curr_resource = input()

    if curr_resource == "stop":
        break
    quantity = int(input())

    if curr_resource not in resourses_dict.keys():
        resourses_dict[curr_resource] = 0
    resourses_dict[curr_resource] += quantity

for resource, quantity in resourses_dict.items():
    print(f"{resource} -> {quantity}")