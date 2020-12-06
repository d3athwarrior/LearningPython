# Dictionaries
# Different ways to declare a dictionary
dict_way_one = {'One': 1, 'Two': 2} # This requires the key, if a string, to be put in double (double) quotes
dict_way_two = dict(One = 1, Two = 2) # This takes in the string as keyword arguments. The part before the = becomes the keys

# Printing the dict
for k, v in dict_way_one.items():
    print(f"Key is {k} and value is {v}")

print('Using key in a for loop')
for k in dict_way_two:
    print(f"Key is {k} and value is {dict_way_two[k]}")

# Sets
# Different ways to declare sets
set_way_one = {1, 2, 3, 4, 5, 3, 'T', 'w'} # This will create a set
set_way_two = set("Hello! This is way two to declare a set")
# This will not work since it will treat the string as a single object rather than multiple characters
# In order for the set to be able to contain a string split into its independent characters we need to have it added using
# the set() constructor
set_way_three = {"Hello! This is a set."}
set_way_two_obj_two = set("Hello! This is a third way to declare a set.")
print(len(set_way_one))
print(len(set_way_two))
print(len(set_way_three))

# Set operations like union, substraction, 
print(f"In set a or set b {set_way_two | set_way_two_obj_two}")
print(f"In set b but not a {set_way_two_obj_two - set_way_two}")
print(f"In either a or b but not both {set_way_two ^ set_way_one}")
print(f"In both a & b {set_way_one & set_way_two}")