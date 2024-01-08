def numbers(number1, number2, number3):
     if number1 < number2 and number1 < number3:
         return number1
     elif number2 < number1 and number2 < number3:
         return number2
     else:
         return number3


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(numbers(num1, num2, num3))