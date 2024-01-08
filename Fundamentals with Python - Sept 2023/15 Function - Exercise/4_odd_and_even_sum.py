def odd_even_sum(number: str) -> str:
    sum_odd_digits = 0
    sum_even_digits = 0
    for i in number:
        if int(i) % 2 == 0:
            sum_even_digits += int(i)
        else:
            sum_odd_digits += int(i)

    return sum_odd_digits, sum_even_digits


number_as_string = input()
sum_odd_digits, sum_even_digits = odd_even_sum(number_as_string)

print(f"Odd sum = {sum_odd_digits}, Even sum = {sum_even_digits}")
