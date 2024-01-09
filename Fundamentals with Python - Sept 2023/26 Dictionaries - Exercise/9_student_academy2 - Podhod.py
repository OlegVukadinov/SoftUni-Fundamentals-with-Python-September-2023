pair_rows = int(input())

my_dict = {}

for curr_pair_row in range(pair_rows):
    student_name = input()
    grade = float(input())

    if student_name not in my_dict:
        my_dict[student_name] = []
    my_dict[student_name].append(grade)

filtered_students = {}
for student_name, grades in my_dict.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        filtered_students[student_name] = average_grade

for name, grades in filtered_students.items():
    print(f"{name} -> {grades:.2f}")


