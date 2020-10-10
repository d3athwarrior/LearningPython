'''
    This is a simple file in which I demonstrate that in order to access a global variable and also use a variable with the same name
    in the local scope of a function I need to use the globals() function to access it. More needs to be learned on how and why but 
    will do when I learn more about scopes.
'''
abcd = "hello"
def myFunction():
    abcd = 5
    globals()['abcd'] = globals()['abcd'] + "#tell python that I am indeed using the global variable and then use it later on !?!?!!!??"
    print(globals()['abcd'])
    print(abcd)
    return

myFunction()

def myFunction2(stringToConcat: str):
    print(abcd+ " " +stringToConcat)
    return

myFunction2("I am a string that was concatanated")