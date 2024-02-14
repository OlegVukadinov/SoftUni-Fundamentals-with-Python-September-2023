def find_smallest(num1, num2, num3):
    smallest = min(num1, num2, num3)
    return smallest


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(find_smallest(num1, num2, num3))