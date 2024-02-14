def numbers(num1, num2):
    factorial_num1 = 1
    factorial_num2 = 1
    for x in range(1, num1 + 1):
        factorial_num1 *= x
    for y in range(1, num2 + 1):
        factorial_num2 *= y
    result = (factorial_num1 / factorial_num2)
    print(f"{result:.2f}")


first_number = int(input())
second_number = int(input())

numbers(first_number, second_number)
