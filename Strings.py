# Strings can be either marked with ' or ". You can use one inside the other without having to escape the characters.

# You can specify the argument position to use for the replacements
person = {'name': 'Anish', 'profession': 'Software Developer'}
x = 'seven {1} {0}'.format(1, 2)
# Doesn't make sense to use the **dict notation here but what it does it that it takes all the values from the dictionary
# and passes them as named arguments to the format function which will eventually lead to matching them with the argument names
y = 'Hi {name}, you are a {profession}'.format(**person)
print('The value of x is {}'.format(x))
print(f'The type of x is {type(x)}') # This 'f' notation is called f string notation where in the format function is called implicitly
print(y)

s = 'Hello this    is a      very long string.'
"""
    This by default will split the string based on the spaces even if there are too many spaces,
    they all will be folded into single space and then split basis of that.
"""
print(s.split())

# join function takes in a list of strings and joins them on the string on which join was called
print(':'.join(s.split()))
