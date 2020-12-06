def main():
    for value in inclusive_range(15):
        print(value, end= " ")
    return

def inclusive_range(*args):
    arg_len = len(args)
    start = 0 # default start point
    step = 1 # default step
    if arg_len < 1:
        raise TypeError(f"Expected at least one argument, got {arg_len}")
    elif arg_len == 1:
        stop = args[0]
    elif arg_len == 2:
        (start, stop) = args
    elif arg_len == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f"Expected max 3 arguments, got {arg_len}")
    
    # The actual range generator
    while start <= stop:
        yield start # This is used to return a function without destroying it's local state
        start += step
    return

if __name__ == "__main__":
    main()