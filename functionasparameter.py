#passing function as a parameter in another function
def display(fun) :
    return "hai" + fun
def msg() :
    return " how are you?"
print(display(msg()))