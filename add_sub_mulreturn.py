def calc(a,b) :

    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return add,sub,mul,div
answer = calc(10,20)

for i in answer :
    print(i)