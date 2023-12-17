def multiplication(num1, num2, num3):
    result = num1 * num2 * num3
    if result > 0:
        return "positive"
    elif result == 0:
        return "zero"
    elif result < 0:
        return "negative"


number1 = int(input())
number2 = int(input())
number3 = int(input())

print(multiplication(number1, number2, number3))
