def var_args(fargs,*vargs) :
    print("formal args",fargs)
    sum = 0
    for i in vargs  :
        sum= sum + i
    print("sum of all numbers",sum)

var_args(10,20,30) 

