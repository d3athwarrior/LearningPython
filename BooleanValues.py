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