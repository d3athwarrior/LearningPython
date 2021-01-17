'''
    This example is to understand how classes behave in python
'''

class Vehicle:
    """
    This is a Vehicle class which can be later used to understand inheritance in python as well. 
    """
    # Usually, when we don't want the user of the class to access the internal or class variable
    # the max we can do in python is to prefix an _ to the variable name to discourage the 
    # consumer of the class from using this variable example instead of wheels we call it _wheels
    # This declaration will usually mean that these objects lie with the class and not with 
    # the object reference
    # Generally, mutable data is never put at the class level. Only constants and immutable data
    # is put at the class level
    #_wheels = 0
    #_type_of_vehicle = ''

    # There are two functions that together do the work of construction of an object
    # 1. __new__
    # 2. __init__
    # It only makes sense to have things in the __init__ block since the work of initializing
    # the object is done in the init method so all the external class variable values that
    # need to be set in the instance should be parsed in the __init__ method itself
    # In python usually something known as Duck Typing is used. But starting with python 3.5,
    # one can to a certain extent in their classes and functions define the type of the
    # object that is returned or is accepted as an argument to the object. This will result
    # the linter to infer those hints and give a warning to the developer to be able to
    # identify issues in the code at the time of writing itself instead of having issues with
    # it at later stages of development
    def __init__(self, wheels: int = 2, type_of_vehicle: str = 'Motor Cycle'):
        # Here the class has _wheels and on the reference as well we are assigning 
        # value to _wheels.
        self._wheels = wheels
        self._type_of_vehicle = type_of_vehicle

    # We need to pass the self variable just because
    # 1. Explicit is better than implicit notion of python
    # 2. So that it can be differentiated as to which is a temp variable 
    # at the method level and which is an instance variable
    # The self parameter can be named anything but it is only preferred to
    # call it self for the sake of convention and easy to understand code
    # The first parameter is infact a reference of the object that is 
    # calling this function
    def number_of_wheels(self):
        return self._wheels

    # If i prefix a function name with __ (double underscore) python performs name mangling, which is explained in the link below:
    # https://dbader.org/blog/meaning-of-underscores-in-python#:~:text=A%20double%20underscore%20prefix%20causes,the%20class%20is%20extended%20later.
    # def __drive
    def drive(self):
        return "The vehicle is being driven around until this program ends."

    def __str__(self):
        return "This vehicle is a " + self._type_of_vehicle + " and it has " + str(self._wheels) + " wheels."

def main():
    '''
        Try to create a main function like how it is in other languages just for the sake of convenience
    '''
    car = Vehicle(4, 'Car')
    bike = Vehicle(2, "Bike")
    print(car._wheels)
    bike._wheels = 3
    print(car._wheels)
    print(Vehicle.drive(car))
    print(car)
    print(car.drive())

if __name__ == "__main__":
    main()
