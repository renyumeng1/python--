n,m = map(int,input().split())
lst = []
for i in range(26):
    lst.append(chr(ord('A')+i))
for i in range(n):
    lst2 = (lst[1:i+1])
    lst3 = lst[0:m-i]
    lst4 = lst2[::-1]+lst3
    for i in lst4[:m]:
        print(i,end='')
    print()
    