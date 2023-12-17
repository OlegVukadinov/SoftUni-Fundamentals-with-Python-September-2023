pair_rows = int(input())

my_dict = {}

for curr_pair_row in range(pair_rows):
    student_name = input()
    grade = float(input())

    if student_name not in my_dict:
        my_dict[student_name] = []
        my_dict[student_name].append(grade)
    else:
        my_dict[student_name].append(grade)

filtered_students = {name: sum(grades) / len(grades) for name, grades in my_dict.items() if sum(grades) / len(grades) >= 4.50}

for name, grades in filtered_students.items():
    print(f"{name} -> {grades:.2f}")


