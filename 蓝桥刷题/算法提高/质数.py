n = eval(input())
lst = []
for i in range(2,n):
    lst.append(i)
    for j in range(2,i):
        if i%j==0:
            lst.pop()
            break
print(len(lst))
for k in lst:
    print(k,end = ' ')
