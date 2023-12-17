number_of_rooms = int(input())

total_free_chairs = 0

for current_room in range(1, number_of_rooms + 1):
    info = input().split()
    num_chairs = int(len(info[0]))
    visitors = int(info[1])

    if num_chairs < visitors:
        print(f"{visitors - num_chairs} more chairs needed in room {current_room}")
        total_free_chairs -= visitors - num_chairs
    elif num_chairs > visitors:
        total_free_chairs += num_chairs - visitors

if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")