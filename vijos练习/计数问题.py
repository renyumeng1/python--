n,x = map(int,input().split())
sum = 0
for i in range(1,n+1):
    if str(x) in str(i):
        b = str(i).count(str(x))
        sum+=b
print(sum)