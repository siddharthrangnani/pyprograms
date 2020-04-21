from array import *
str = input("enter marks")
marks=[int(num) for num in str]
sum=0
for x in marks:
    print(x)
    sum+=x
    print(sum)
n=len(marks)
perc=sum/n
print(perc)
