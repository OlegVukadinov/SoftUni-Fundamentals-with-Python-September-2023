def sum_numbers(number1, number2):
    result = number1 + number2
    return result
def subtract(result, number3):
    result2 = result - number3
    return result2
def add_and_subtract(number1, number2, number3):
    result = sum_numbers(number1, number2)
    result2 = subtract(result, number3)
    print(result2)


num1 = int(input())
num2 = int(input())
num3 = int(input())

add_and_subtract(num1, num2, num3)