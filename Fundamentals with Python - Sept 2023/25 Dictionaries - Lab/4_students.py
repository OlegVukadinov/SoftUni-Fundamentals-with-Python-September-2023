students = []
searched_course = None

while True:
    students_info = input()

    if ":" not in students_info:
        searched_course = students_info
        break

    name, ID, course = students_info.split(":")
    students.append({'name': name, 'ID': ID, 'course': course})

for student in students:
    if searched_course.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['ID']}")