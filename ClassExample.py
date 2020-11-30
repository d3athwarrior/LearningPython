'''
    This example is to understand how classes behave in python
'''

class Vehicle:
    """
    This is a Vehicle class which can be later used to understand inheritance in python as well. 
    """
    wheels = 0
    type_of_vehicle = ''

    # There are two functions that together do the work of construction of an object
    # 1. __new__
    # 2. __init__
    # It only makes sense to have things in the __init__ block since the work of initializing
    # the object is done in the init method so all the external class variable values that
    # need to be set in the instance should be parsed in the __init__ method itself
    def __init__(self, wheels = 2, type_of_vehicle = 'Motor Cycle'):
        self.wheels = wheels
        self.type_of_vehicle = type_of_vehicle

    # We need to pass the self variable just because
    # 1. Explicit is better than implicit notion of python
    # 2. So that it can be differentiated as to which is a temp variable 
    # at the method level and which is an instance variable
    def number_of_wheels(self):
        return self.wheels

    # If i prefix a function name with __ (double underscore) python performs name mangling, which is explained in the link below:
    # https://dbader.org/blog/meaning-of-underscores-in-python#:~:text=A%20double%20underscore%20prefix%20causes,the%20class%20is%20extended%20later.
    def __drive(self):
        return "The vehicle is being driven around until this program ends."

    def __str__(self):
        return "This vehicle is a " + self.type_of_vehicle + " and it has " + str(self.wheels) + " wheels."

def main():
    '''
        Try to create a main function like how it is in other languages just for the sake of convenience
    '''
    car = Vehicle(4, 'Car')
    print(Vehicle.drive(car))
    print(car)
    print(car.drive())

if __name__ == "__main__":
    main()
