def flag(m,n):
    for j in range(len(n)-2):
        if n[j+1]>=n[j] or m[j]<=n[j]:
            return False
        return True
from itertools import permutations
lst = [x for x in range(1,2021)]
a = list(permutations(lst))
lst1 = a[0:len(a)//2]
lst2 = a[len(a)//2:]
count = 0
if flag(lst1,lst2) or flag(lst2,lst1):
    count+=1
print(count%2020)
        