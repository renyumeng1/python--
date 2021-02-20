from itertools import permutations
lst = [1,2,3,4,5,6,7,8,9]
box = list(permutations(lst))
ans = 0
def flag(lst):
    n = lst[1]*10+lst[2]
    m= lst[4]*10+lst[5]
    p = lst[7]*10+lst[8]
    if lst[0]*m*p+lst[3]*n*p==lst[6]*n*m:
        return True
    return False
for i in box:
    if flag(i):
        ans+=1
print(ans/2)