from time import time
from Generator import inclusive_range
from datetime import datetime
from functools import wraps

# Decorators in python can be applied in the following scenarios
# 1. Timing
# 2. 
# More on decorators https://www.youtube.com/watch?v=MjHpMCIvwsY&feature=youtu.be
def logtime(decorated_function):
    # More on the wraps decorator inbuilt in python
    # https://dbader.org/blog/python-decorators#:~:text=Python's%20decorators%20allow%20you%20to,great%20use%20case%20for%20decoration.
    # https://docs.python.org/3/library/functools.html
    # When a function is decorated, the original meta data is lost. In order to preserver that,
    # python has provided this innbuilt decorator called 'wraps' to retain the original meta data
    @wraps(decorated_function)
    # An inner wrapper is needed in case we want to pass value to the inner function being called
    def wrapper(count):
        # if we want a more human readable form of the time we can use the datetime.now() function and get the time
        # in HH.mm.ss.microseconds
        execution_start = time()
        print(f"Execution started at {execution_start}")
        original_result = decorated_function(count)
        print(f"Execution completed in {time() - execution_start}")
        return original_result
    return wrapper

# logtime is a decorator
# Multiple decorators can be applied to one function
@logtime
def add_numbers(count):
    '''
        Simple function that adds numbers from 1 to count
    '''
    if count < 1:
        raise TypeError(f"Expected count to be at least 1 but got {count}")
    total = 0
    for num in inclusive_range(count):
        total += num
    return total


if __name__ == "__main__":
    print(add_numbers(500000))