def calculates(action:str, num1:int, num2:int):
    global result
    if action == "multiply":
        result = a * b
    elif action == "divide":
        result = a / b
    elif action == "add":
        result = a + b
    elif action == "subtract":
        result = a - b
    return f"{result:.0f}"

operator = input()
a = int(input())
b = int(input())
print(calculates(operator, a, b))