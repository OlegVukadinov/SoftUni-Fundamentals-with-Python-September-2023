from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus  = int(input())

max_lectures = 0
max_bonus = 0

for curr_student in range(1, number_of_students + 1):
    count_of_attendances = int(input())

    total_bonus = count_of_attendances / number_of_lectures * (5 + additional_bonus)

    if total_bonus > max_bonus:
        max_bonus = total_bonus
    if count_of_attendances > max_lectures:
        max_lectures = count_of_attendances

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {ceil(max_lectures)} lectures.")