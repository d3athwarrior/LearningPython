from decimal import Decimal
number = .1 + .1 + .1 - 0.3 # There will be precision but the accuracy is lost in this calculation
print(number)
print(type(number))

# To solve the above problem, the decimal library needs to be used
# It is needed to use special library especially when dealing with currency
a = Decimal('0.1')
b = Decimal('0.3')
result = a + a + a - b
print(result)
print(type(result)) # The result will be of type decimal.Decimal instead of being a float