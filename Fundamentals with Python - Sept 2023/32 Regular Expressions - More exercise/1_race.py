import re

participants = input().split(", ")
racers = {}

while True:
    line = input()
    if line == "end of race":
        break

    match = re.findall(r'([A-Za-z]+)', line)
    racer_name = ''.join(match)

    distance = 0

    if racer_name in participants:
        match_dist = re.findall(r'(\d)', line)
        for digit in match_dist:
            distance += int(digit)
        racers[racer_name] = racers.get(racer_name, 0) + distance

    # Sort racers by distance in descending order
sorted_racers = sorted(racers.items(), key=lambda x: x[1], reverse=True)

    # Print top 3 racers
print(f"1st place: {sorted_racers[0][0]}")
print(f"2nd place: {sorted_racers[1][0]}")
print(f"3rd place: {sorted_racers[2][0]}")


