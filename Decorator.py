from time import sleep, time
from Generator import inclusive_range
from functools import wraps

# Decorators in python can be applied in the following scenarios
# 1. Timing
# 2. Limiting the number of times a function can be executed in a given time frame
# 3. Memoization - caching the result of a call when the arguments are same as previous time
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

# This decorator will make sure that a function is only called once per 'time_before_next_call'
def call_only_once_n(seconds_before_next_call):
    """
    Call only once per time_before_next_call
    """
    def track_last_called(decorated_function):
        """
        Additional decorator to maintain state of the last time the decorated function was called
        """
        last_invoked = 0
        def wrapper(sum_to):
            """
            The wrapper that will actually wrap the decorated_function
            """
            nonlocal last_invoked
            if time() - last_invoked < seconds_before_next_call:
                raise AssertionError("Called too soon!")
            last_invoked = time()
            return decorated_function(sum_to)
        return wrapper
    return track_last_called

# logtime is a decorator
# call_only_once_n is also a decorator
# Multiple decorators can be applied to one function
@logtime
@call_only_once_n(5)
def add_numbers(sum_to):
    '''
        Simple function that adds numbers from 1 to count
    '''
    if sum_to < 1:
        raise TypeError(f"Expected count to be at least 1 but got {sum_to}")
    total = 0
    for num in inclusive_range(sum_to):
        total += num
    return total


if __name__ == "__main__":
    # print(add_numbers(500000))
    print(add_numbers(10))
    sleep(5)
    print(add_numbers(150))