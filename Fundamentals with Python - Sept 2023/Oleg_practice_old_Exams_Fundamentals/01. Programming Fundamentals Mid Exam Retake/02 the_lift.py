def fill_lift(people_waiting, current_state):
    current_state = [int(wagon) for wagon in current_state.split()]
    for i in range(len(current_state)):
        while current_state[i] < 4 and people_waiting > 0:
            current_state[i] += 1
            people_waiting -= 1

    return current_state, people_waiting


people_waiting = int(input())
current_state = input()

final_state, remaining_people = fill_lift(people_waiting, current_state)

if remaining_people == 0 and sum(final_state) < len(final_state) * 4:
    print("The lift has empty spots!")
    print(" ".join(map(str, final_state)))
elif remaining_people > 0 and sum(final_state) == len(final_state) * 4:
    print(f"There isn't enough space! {remaining_people} people in a queue!")
    print(" ".join(map(str, final_state)))
else:
    print(" ".join(map(str, final_state)))