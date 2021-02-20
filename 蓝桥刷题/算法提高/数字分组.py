lst = [eval(x) for x in input().split()]
lst.sort()
x = lst[0:3]
y = lst[3:6]
z = lst[6:]
print(sum(x)/len(x))
print(sum(y)/len(y))
print(round(sum(z)/len(z),3))