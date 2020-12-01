# Please look at the other files for more elaborate idea on how if else work in Python.
# In this I will cover the conditional operators and conditional assignment only

# Ternary operator syntax in python
# Using bool(input("The earth is round: True or False")) will always result in true since strings with values always evaluate to true in python
condition = input("The earth revolves around the sun: True or False")

# Below is an example of how ternary operators are written in python
print("Congratulations!! You have passed" if condition == 'True' else "The person has failed test.")