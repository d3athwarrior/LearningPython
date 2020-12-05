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
# help(add)

test_passing_function_as_arguments(add, subtract) # We can pass functions to another function for execution

# We can assign a function to another variable and then call it using that
# https://medium.com/python-pandemonium/function-as-objects-in-python-d5215e6d1b0d
renamed_add_function = add
print(renamed_add_function(85, 10))


# In python, immutable objects like list are pass by reference when passed to a function
# Values like integer and string are immutable and hence, are passed by value
def passByValue(randomNumber):
    randomNumber = 15
    print(randomNumber)
    return

def passByReference(listOfNames):
    listOfNames[0] = "Bunny"
    print(f"The list of names in reference is {listOfNames}")
    return

def main():
    number = 11
    print(f"The value of 'number' is {number}")
    passByValue(number)
    print(f"The value of 'number' has not changed and is {number}")
    listOfNames = ["Tortoise", "Rabbit", "Horse"]
    print(f"The list of names before passing around is {listOfNames}")
    passByReference(listOfNames)
    print(f"The list of names post passing around is {listOfNames}")
    return


# Python script is read from top to bottom, so any function that needs to be called,
# needs to be defined before the statement for it's call appears in the script.
if __name__ == "__main__":
    '''
        This check is similar to how main function behaves in many of the other languages
        But since python is a scripting language, it doesn't really have a main function or
        a so called starting point of execution

        If a file is not in a module or imported in a module, then the __name__ will always
        return __main__ indicating that it is either the first file that was executed
        or it was the only file that was executed
    '''
    main()
    # All functions in python return a value. When no specific value is returned,
    # The special None value is returned as seen below
    print(renamed_add_function())
