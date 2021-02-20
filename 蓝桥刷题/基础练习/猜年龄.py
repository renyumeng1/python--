from itertools import permutations
lst = ['0','1','2','3','4','5','6','7','8','9']
fl = tuple(permutations(lst))
def flag(n,fl):
    fi = str(n**3)
    se = str(n**4)
    tr = fi+se
    li = [x for x in tr]
    if tuple(li) in fl:
        return True
    return False
for i in range(10,20):
    if flag(i,fl):
        print(i)
    