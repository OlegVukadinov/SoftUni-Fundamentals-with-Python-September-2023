number_snowballs = int(input())
max_weight = 0
max_needed_time = 0
max_quality = 0
max_value = 0
for current_snowball in range(1, number_snowballs + 1):
    weight = int(input())
    needed_time = int(input())
    quality = int(input())

    value = (weight / needed_time) ** quality

    if value > max_value:
        max_value = value
        max_weight = weight
        max_needed_time = needed_time
        max_quality = quality

print(f"{max_weight} : {max_needed_time} = {int(max_value)} ({max_quality})")