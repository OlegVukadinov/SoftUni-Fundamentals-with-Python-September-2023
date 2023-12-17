sequence_of_numbers = list(map(int, input().split(", ")))
current_group = 10
while sequence_of_numbers:
    filtered_sequence_of_numbers_for_current_group = [num for num in sequence_of_numbers if num <= current_group]
    print(f"Group of {current_group}'s: {filtered_sequence_of_numbers_for_current_group}")
    current_group += 10
    sequence_of_numbers = [num for num in sequence_of_numbers if num not in filtered_sequence_of_numbers_for_current_group]




