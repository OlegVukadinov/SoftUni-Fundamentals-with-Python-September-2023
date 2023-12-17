def calculates(text, num1, num2):
    if text == "multiply":
      result = num1 * num2
    elif text == "divide":
      result = int(num1 / num2)
    elif text == "add":
      result = num1 + num2
    elif text == "subtract":
      result = num1 - num2
    return result

command = input()
number1 = int(input())
number2 = int(input())

print(calculates(command, number1, number2))
