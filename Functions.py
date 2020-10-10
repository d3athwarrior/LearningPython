def add(num1: float = 0, num2: float = 0):
    return num1 + num2

def subtract(num1: float = 0, num2: float = 0):
    return num1 - num2

def multiply(num1: float = 0, num2: float = 0):
    return num1 * num2

def divide(num1: float = 0, num2: float = 0):
    return num1 / num2


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(add(num1, num2))
print(subtract(num1, num2))
print(multiply(num1, num2))
print(divide(num1, num2))