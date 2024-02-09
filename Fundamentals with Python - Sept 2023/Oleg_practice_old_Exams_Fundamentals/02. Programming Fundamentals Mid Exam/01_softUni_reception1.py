employee1_stud_per_hour = int(input())
employee2_stud_per_hour = int(input())
employee3_stud_per_hour = int(input())
number_students = int(input())
time_needed = 0

while True:
    if number_students <= 0:
        print(f"Time needed: {time_needed}h.")
        break

    efficiency_per_hour = employee1_stud_per_hour + employee2_stud_per_hour + employee3_stud_per_hour
    number_students -= efficiency_per_hour
    time_needed += 1

    if time_needed % 4 == 0:
       time_needed += 1


