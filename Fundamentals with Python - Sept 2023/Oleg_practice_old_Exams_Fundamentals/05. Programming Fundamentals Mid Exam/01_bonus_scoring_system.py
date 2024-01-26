from math import ceil
number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

total_bonus = 0
max_total_bonus = 0
max_attendance_each_student = 0

for current_student in range (1,number_of_students + 1 ):
    attendance_each_student = int(input())

    total_bonus = attendance_each_student / number_of_lectures * (5 + additional_bonus)

    if total_bonus > max_total_bonus:
        max_total_bonus = total_bonus
    if attendance_each_student > max_attendance_each_student:
        max_attendance_each_student = attendance_each_student

print(f"Max Bonus: {ceil(max_total_bonus)}.")
print(f"The student has attended {ceil(max_attendance_each_student)} lectures.")
