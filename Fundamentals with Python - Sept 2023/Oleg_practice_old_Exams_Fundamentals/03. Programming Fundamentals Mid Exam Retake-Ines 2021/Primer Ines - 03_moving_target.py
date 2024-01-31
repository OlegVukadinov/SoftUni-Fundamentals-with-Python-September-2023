def check_if_index_is_valid(index, len_list):  # Проверяваме дали индекса е валиден
    if index in range(len_list):
        return True
    else:
        return False


target_list = list(map(int, input().split()))

while True:
    command = input()

    if command == "End":
        #print('|'.join([str (el) for el in target_list]))
        break

    action, index, value = command.split()
    index = int(index)
    value = int(value)

    if action == "Shoot":
        if check_if_index_is_valid(index, len(target_list)):
            target_list[index] -= value
            if target_list[index] <= 0:
                target_list.pop(index)  # Махаме елемента от този индекс, но не можем да използваме remove
                # защото не знаем кой е елемента и затова използваме рор(index)
    elif action == "Add":
        if check_if_index_is_valid(index, len(target_list)):
            target_list.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        left_most_index = index - value
        right_most_index = index + value
        if check_if_index_is_valid(index, len(target_list)) and check_if_index_is_valid(left_most_index,len(target_list))and check_if_index_is_valid(right_most_index, len(target_list)):
            left_unstriked_part = target_list[0:left_most_index]  # target_list.pop(index)
            right_unstriked_part = target_list[right_most_index + 1:]
            target_list = left_unstriked_part + right_unstriked_part

        else:
            print("Strike missed!")

print('|'.join([str (el) for el in target_list]))
