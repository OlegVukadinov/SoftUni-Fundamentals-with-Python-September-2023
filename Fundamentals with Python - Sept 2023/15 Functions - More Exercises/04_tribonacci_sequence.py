def tribonacci_seq(number):
    final_list = [1]
    for current_number in range(1, number):
        if len(final_list) < 3:
            final_list.append(current_number)
        else:
            final_list.append(sum(final_list[-3:]))

    return ' '.join([str(num) for num in final_list])


num = int(input())

print(tribonacci_seq(num))