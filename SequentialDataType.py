x = [ 1, 4, 6, 7, 10] # This is an array/list
for value in x:
    print(value)
x[4] = 55
# x[-6] = 15 # Just like regular access, if the negative index is out of range then it will throw error
for value in x:
    print(value)
print(type(x))
# This is a tuple and it is immutable
y = ( 15, 17, 19)
for value in y:
    print(value)
# y[2] = 95 # This line will give error
print(y)


# range can also be used to create sequential data
z = range(5,100, 9) # Start, end, increment. Default increment is by 1
print("Range is: " + str(z)) # I expect this to print an array kind of but it just prints the object value. Need to find out why it is this way
for val in z:
    print(val)
print(type(z))
# z[1] = 100 # This will give error as the range object doesn't support modification
list_var = list(z) # convert a range into a list so that it can be modified. You cannot modify a range object directly
list_var[3] = 5847
for listVal in list_var:
    print(listVal)

# There is also dictionary but I already have understood it else where