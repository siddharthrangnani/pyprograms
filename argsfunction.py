def add(fargs,*args):
    print("formal args",fargs)
    sum = 0
    for i in args:
        sum+=i
    print("sum",(fargs+sum))
add(20,30,40)