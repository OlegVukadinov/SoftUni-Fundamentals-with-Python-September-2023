teamA = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
teamB = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
counter_A = 11
counter_B = 11
card = input().split()

for element in (card):

    if element in teamA:
        counter_A -= 1
        teamA.remove(element)
    if element in teamB:
        counter_B -= 1
        teamB.remove(element)

    if counter_A < 7 or counter_B < 7:
        break

print(f"Team A - {counter_A}; Team B - {counter_B}")
if counter_A < 7 or counter_B < 7:
    print("Game was terminated")
