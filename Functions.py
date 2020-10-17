def add(num1: float = 1, num2: float = 0):
    # A function's doc string will always be inside it rather than on top of it
    '''
        This function will add the two numbers passed to it
    '''
    return num1 + num2

def subtract(num1: float = 1, num2: float = 0):
    return num1 - num2

def multiply(num1: float = 2, num2: float = 0):
    return num1 * num2

def divide(num1: float = 0, num2: float = 0):
    return num1 / num2

def test_passing_function_as_arguments(funct1, funct2):
    print(funct1(1,2))
    print(funct2(1,3))

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(add(num1, num2))
print(subtract(num1, num2))
print(multiply(num1, num2))
print(divide(num1, num2))

# Do not pass any value to the function here
print(add())

# Pass the value to specific parameter
print(add(num2=45))

# Named arguments for function, due to which order of the parameters passed doesn't matter
print(add(num2=55, num1= 5))

# Print the docstring for a function
help(add)

test_passing_function_as_arguments(add, subtract) # We can pass functions to another function for execution