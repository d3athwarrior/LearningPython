from decimal import DivisionByZero
from sys import exc_info
from traceback import print_exc, print_exception

def main():
    print("Learning Exceptions")
    '''
        Try can be with catch and multi catch
    '''
    try:
        x = 5/0
        # x = int("potato")
        '''
            If I purposefully raise an exception in the try block unconditionally then in that case,
            the else block will never be executed which is understandable since 
            the try block is always going raise and exception
        '''
        # raise BaseException("Hello this is a exception of type base")
    except ValueError as error:
        print("Error in the value")
    except DivisionByZero as e:
        '''
            Since I come from a Java Background, I understand why this is an okay way if not better than
            the one below this block
        '''
        print(f'{e.args} {print_exception()}')
    except (Exception, BaseException) as e:
        '''
            This block depicts how I can catch multiple exceptions in a single except block
        '''
    except:
        '''
            For when we don't know what error is going to be thrown by the logical block.
            This is considered a bad practice since this will usually catch almost all the errors and
            exceptions that we may not want to catch at all.
        '''
        print(exc_info()[0])
    else:
        '''
            This block is actually executed only when there is no exception
        '''
        print('Hooray! My program executed successfully')
    finally:
        print("This block is exected irrespective of what exception is thrown from above")

if __name__ == "__main__":
    main()