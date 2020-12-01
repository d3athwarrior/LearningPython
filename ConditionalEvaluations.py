'''
    Checking whether python is like JS while comparision to automatically convert the variables to be able to compare them
'''
string = '12'
print(12 == string) # This will return false as the variable string is treated as a string rather than an integer

# -----------------------------------------------------------------------------------------------------------------
print(12.0 == 12) # While comparing it here, the integer 12 will be converted automatically to float type but if we do a simple 
                  # Type verification we will see that it will return float for 12.0 and integer for 12