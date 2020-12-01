secret = "fish"
password = ""
authorized = False
count = 0
max_Count = 5

while password != secret:
    password = input("What's the password?")
else:
    # The else block in case of a loop, be it for loop or while loop will always be executed with exception of the case when 'break' is used to come out of the loop
    print("In else block")

# in other languages one can iterate using an index but in case of python we use 'enumerate' to be able to fetch the
# natural index (starting with 1) along with the value. This will not be the true index of an item 
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson", "Jones"]
countries = ["India", "Japan", "China", "USA", "Germany"]
for num, name in enumerate(presidents, start=1):
    print("President {}: {}".format(num, name))
    print(presidents[num-1]) # this will give an error if the -1 is not done

# zip function iterates only as many number of times as the number of items in the shortest of the lists that are passed to the zip function
for president, country in zip(presidents,countries):
    print(president, country)