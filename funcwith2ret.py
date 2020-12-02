def sum(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e

t=sum(4,5)
for i in t:
    print(i)

def func1(str):
   return 'hai' + str
def func2():
    return "How are you"
print(func1(func2()))
def heap(a):
    return id(a)

print(heap(10))