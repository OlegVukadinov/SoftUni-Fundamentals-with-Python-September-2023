number_people = int(input())
capacity = int(input())
counter_courses = 0

while number_people > 0:
    number_people -= capacity
    counter_courses += 1

print(f"{counter_courses}")