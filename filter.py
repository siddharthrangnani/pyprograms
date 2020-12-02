def oddeve(x) :
    if x%2==0:
        return True
    else :
        return False
lst=[10,20,34,53,234,3,34,230]
lst1=list(filter(oddeve,lst))
print(lst1)