# Python understands truthy values and falsy values instead of explicitly evaluating true and false only
random_dict = {'a': 1}
empty_dictionary = {}
empty_string = ''

if random_dict:
    print("random_dict evaluated to true")
else:
    print("random_dict evaluated to false")

if empty_string:
    print('Empty string evaluated to true')
else:
    print('Empty string evaluated to false')

if 0:
    print('Zero is evaluated as true')
else:
    print('Zero is evaluated as false')

if None:
    print('None is evaluated as true')
else:
    print('None is evaluated as false')

if empty_dictionary:
    print('empty_dictionary is evaluated as true')
else:
    print('empty_dictionary is evaluated as false')

# In essence, everything that is eventually empty is treated as false including 0 and everything else is treated as true or as 'it exists'

# Boolean operators
# Boolean operators in python are literal english text equivalent like and, or, not, in, not in, etc.
# Additionally, there is "is" and "is not" which is for verifying object identity

inputOne = True
inputTwo = False

# And operator
print("Value of a and b: ", inputOne and inputTwo)

# Or operator
print("Value of a or b: ", inputOne or inputTwo)

# not operator
# It is a single operand operator similar to how !(not) in other languages
print("Value of not a: ", not inputOne)

# in - used with sets
valueSet = (1, 2, 3, 4, 5) # Tuple with random values
valueToMatch = 3
print("valueToMatch in valueSet:", valueToMatch in valueSet)

# not in - used with sets
print("valueToMatch not in valueSet:", valueToMatch not in valueSet)

# is - verify object identity
print("valueToMatch is valueSet:", valueToMatch is valueSet)

# not is - verify object identity
print("valueToMatch is not valueSet:", valueToMatch is not valueSet)

# Always prefer to use parenthesis to explicitly specify the precedence so that it can be easily understood by another programmer
# Refer to operator precedence python doc for the chart