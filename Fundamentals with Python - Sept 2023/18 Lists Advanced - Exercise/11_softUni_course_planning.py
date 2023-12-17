schedule = input().split(', ')
index = 1

def add_lesson(lesson, current_schedule):
    if lesson not in current_schedule:
        current_schedule.append(lesson)

def insert_lesson(lesson, current_schedule, idx):
    if lesson not in current_schedule:
        current_schedule.insert(idx, lesson)

def remove_lesson(lesson, current_schedule):
    if lesson in current_schedule:
        current_schedule.remove(lesson)

def swap_lessons(lesson1, lesson2, current_schedule):
    if lesson1 in current_schedule and lesson2 in current_schedule:
        idx1 = current_schedule.index(lesson1)
        idx2 = current_schedule.index(lesson2)
        current_schedule[idx1], current_schedule[idx2] = current_schedule[idx2], current_schedule[idx1]

def add_exercise(lesson, current_schedule):
    if lesson in current_schedule:
        idx = current_schedule.index(lesson)
        exercise = f"{lesson}-Exercise"
        if idx + 1 < len(current_schedule) and not current_schedule[idx + 1].endswith("-Exercise"):
            current_schedule.insert(idx + 1, exercise)
        else:
            current_schedule.append(exercise)

while True:
    command = input()
    if command == "course start":
        break

    action, *args = command.split(':')

    if action == "Add":
        add_lesson(args[0], schedule)
    elif action == "Insert":
        insert_lesson(args[0], schedule, int(args[1]))
    elif action == "Remove":
        remove_lesson(args[0], schedule)
    elif action == "Swap":
        swap_lessons(args[0], args[1], schedule)
    elif action == "Exercise":
        add_exercise(args[0], schedule)

for lesson in schedule:
    print(f"{index}.{lesson}")
    index += 1
