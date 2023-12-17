def exchange(lst, index):
    if index < 0 or index >= len(lst):
        print("Invalid index")
        return lst
    return lst[index + 1:] + lst[:index + 1]

def find_max_even_odd(lst, command):
    is_even = command == "max even"
    filter_func = lambda x: x % 2 == 0 if is_even else x % 2 != 0
    max_element = None
    max_index = -1
    for i in range(len(lst)):
        if filter_func(lst[i]):
            if max_element is None or lst[i] >= max_element:
                max_element = lst[i]
                max_index = i
    return max_index

def find_min_even_odd(lst, command):
    is_even = command == "min even"
    filter_func = lambda x: x % 2 == 0 if is_even else x % 2 != 0
    min_element = None
    min_index = -1
    for i in range(len(lst)):
        if filter_func(lst[i]):
            if min_element is None or lst[i] <= min_element:
                min_element = lst[i]
                min_index = i
    return min_index

def first_last_even_odd(lst, command, count):
    is_even = command.endswith("even")
    filter_func = lambda x: x % 2 == 0 if is_even else x % 2 != 0
    filtered_lst = [x for x in lst if filter_func(x)]

    if len(filtered_lst) == 0:
        return "[]"

    if command.startswith("first"):
        return filtered_lst[:count]
    else:
        return filtered_lst[-count:]

# Read the initial list
initial_list = list(map(int, input().split()))

# Process the commands
while True:
    command = input().strip()

    if command == "end":
        break

    if command.startswith("exchange"):
        index = int(command.split()[1])
        initial_list = exchange(initial_list, index)
    elif command.startswith("max"):
        max_index = find_max_even_odd(initial_list, command)
        if max_index != -1:
            print(max_index)
        else:
            print("No matches")
    elif command.startswith("min"):
        min_index = find_min_even_odd(initial_list, command)
        if min_index != -1:
            print(min_index)
        else:
            print("No matches")
    elif command.startswith("first") or command.startswith("last"):
        count = int(command.split()[1])
        if count > len(initial_list):
            print("Invalid count")
        else:
            result = first_last_even_odd(initial_list, command, count)
            print(result)

# Print the final list
print(f"[{', '.join(map(str, initial_list))}]")