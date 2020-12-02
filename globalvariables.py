#local variable
def func():
    a=2
    print(a)
print()
func()
b=32
#global variable
def fun():
    print(b)
fun()
print(b)
# using global keyword
e=5
def glob():
    global e
    e=3
    print(e)
glob()
print(e)
#using globals keyword
a=11
def globalss():
    a=2
    print("local",a)
    x=globals()['a']
    print(x)
globalss()