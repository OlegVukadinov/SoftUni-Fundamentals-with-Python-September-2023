def odd_even_sum(num):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for el in num:
        if int(el) % 2 == 0:
            sum_of_even_digits += int(el)
        else: # int(el) % 3 == 0:
            sum_of_odd_digits += int(el)
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

number = input()
print(odd_even_sum(number))