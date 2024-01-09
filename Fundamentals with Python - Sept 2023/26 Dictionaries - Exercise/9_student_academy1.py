n_rolls = int(input())

data_dict = {}

for curr_roll in range(1, n_rolls + 1):
    name = input()
    grade = float(input())

    if name not in data_dict.keys():
        data_dict[name] = []
        data_dict[name].append(grade)
    else:
        data_dict[name].append(grade)

for name, grade in data_dict.items():
    average_grade = sum(data_dict[name]) / len(data_dict[name])
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")