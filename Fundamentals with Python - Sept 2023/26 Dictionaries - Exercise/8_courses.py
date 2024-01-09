course_dict = {}

while True:
    command = input()

    if command == "end":
        break
    data = command.split(" : ")
    course_name = data[0]
    student_name = data[1]

    if course_name not in course_dict:
        course_dict[course_name] = []
    course_dict[course_name].append(student_name)

for course_name, registered_students in course_dict.items():
    print(f"{course_name}: {len(registered_students)}")
    for student in registered_students:
        print(f"-- {student}")