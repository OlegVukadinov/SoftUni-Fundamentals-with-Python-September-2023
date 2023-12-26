sequence_of_numbers = input().split()

for i in range(len(sequence_of_numbers)):  # превръщаме списъка със стринговете в списък с интеджери
    sequence_of_numbers[i] = int(sequence_of_numbers[i])
    
middle = len(sequence_of_numbers) // 2

left_car = sequence_of_numbers[0:middle]
right_car = sequence_of_numbers[-1:middle:-1]

left_car_time = 0
right_car_time = 0

for curr_time in left_car:
    left_car_time += curr_time
    if curr_time == 0:
        left_car_time *= 0.8

for curr_time in right_car:
    right_car_time += curr_time
    if curr_time == 0:
        right_car_time *= 0.8


if left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
elif left_car_time > right_car_time:
    print(f"The winner is right with total time: {right_car_time:.1f}")
