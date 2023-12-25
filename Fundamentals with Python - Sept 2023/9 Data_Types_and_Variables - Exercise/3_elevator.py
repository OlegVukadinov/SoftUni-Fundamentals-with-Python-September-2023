number_people = int(input())
capacity = int(input())
counter_courses = 0
counter_people = 0

while number_people >= 0:
    counter_courses += 1
    counter_people += capacity

    if counter_people >= number_people:
        break

print(f"{counter_courses}")