def even_nums(nums):
    my_list = []
    for el in nums:
        if el % 2 == 0:
            my_list.append(el)
    return my_list

numbers = list(map(int, input().split()))
print(even_nums(numbers))