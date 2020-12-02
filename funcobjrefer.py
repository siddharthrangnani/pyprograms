# int str float are immutatable so objects cannot be modified and new reference is created for same
def modify(x):
    x=10
    print(x,id(x))
x=15
modify(x)
print(x,id(x))
#list is immutable
def modifyy(lst):
    lst.append(9)
    print(lst,id(lst))
lst=[1,2,3,4]
modifyy(lst)
print(lst,id(lst))