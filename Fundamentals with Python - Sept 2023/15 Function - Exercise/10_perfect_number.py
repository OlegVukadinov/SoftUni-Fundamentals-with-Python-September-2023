def perfect_number(num:int):
    sum_counter = 0
    for cur_num in range(1, num):
        if num % cur_num == 0 and cur_num > 0:
            sum_counter += cur_num
    if num == sum_counter:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

number = int(input())
print(perfect_number(number))