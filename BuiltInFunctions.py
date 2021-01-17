# Further reference of the inbuilt functions in python can be found at https://docs.python.org/3.9/library/functions.html

floatId = float('200045675') # constructor of the float data type
number = -15
print(floatId)
print('Absolute value is {}'.format(abs(number)))

""" 
    divmod returns the quotient and the remainder of the division operation
"""
print('The result of division is {}'.format(divmod(floatId, number)))

# String functions
# 1. repr - basically does the job of representing a value or object as a string
# 2. ascii
# 3. ord
# 4. chr

class Demo:
    def __init__(self, number_of_demo: int):
        self._number_of_demo = number_of_demo
    
    def __str__(self) -> str:
        return f'This object has {self._number_of_demo} objects.'
    
    """ 
        when the repr function is called on an object, the repr function of the object is called.
        In case we want the representation to be correctly shown when the repr function is called
        on the object then in that case we must override the __repr__ function and return a string
    """
    def __repr__(self) -> str:
        return self.__str__() + ' Normal repr 🖖'

obj = Demo('11')
"""
    The repr function will always look for a repr function in the class.
    Calling the print function with the object passed as a parameter will
    result in first the function looking for the __str__ function and if not found,
    it will call the __repr__ function

    So in the above class if we comment out the __str__ function we will see that
    whatever is returned from the __repr__ function will be printed
"""
print(repr(obj))
print(obj)
"""
    Calling the ascii function on the object will inturn call the __repr__
    itself but then it will simply escape all the non ascii characters and print the string
"""
print(ascii(obj))

print(ord('🖖')) # returns the unicode number of the passed character
print(chr(128407)) # Returns the unicode symbol of the number passed to the function

# Collection functions
simpleTuple = (1, 2, 3, 5, 'Hello')
anotherTupleForZipping = (4, 5, 6, 7)
"""
    Reversed usually returns an iterator hence we need to put it into a type or should print it using a for loop
"""
reverse = list(reversed(simpleTuple))

print(f'Original tuple is: {simpleTuple}')
print(f'Modified tuple is: {reverse}')

# print(max(simpleTuple)) # This will not work since the tuple has some non number values as well
# print(min(simpleTuple)) # This will not work as well due to the above reason

"""
    any() returns true if any one value of the entire set of the object is truthy
    all() returns true if all of the values are truthy
"""
print(any(simpleTuple))

"""
    zip() pairs the iterable values and combines them into the shortest of them all which can then be used anyway one needs to
    notice that there are only 4 values that are returned from the zip function which is due to anotherTupleForZipping containing
    only 4 values
"""
for val1, val2 in zip(simpleTuple, anotherTupleForZipping):
    print(f'{val1} - {val2}')

"""
    enumerate() returns the enumeration of the iterable with the index and the value
"""