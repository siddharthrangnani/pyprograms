def calc(lst):
    s_add = 0
    for i in lst :
        s_add = s_add + i
    return s_add
       
        
lst = [int(x) for x in input().split(" ")]
ans = calc(lst)
print(ans)