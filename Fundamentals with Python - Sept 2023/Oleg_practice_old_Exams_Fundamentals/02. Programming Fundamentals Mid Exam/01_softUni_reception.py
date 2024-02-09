emp1 = int(input())
emp2 = int(input())
emp3 = int(input())
num_students = int(input())
counter_time = 0
while num_students > 0:
    answered_students_per_hour = emp1 + emp2 + emp3
    num_students -= answered_students_per_hour
    counter_time += 1

    if counter_time % 4 == 0:
        counter_time += 1

print(f"Time needed: {counter_time}h.")