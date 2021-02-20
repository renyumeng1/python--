def gcd(a,b):
    x = max(a,b)
    y= min(a,b)
    r = x%y
    if r==0:
        return y
    else:
        while r!=0:
            x = y
            y = r
            r = x%y
        return y
cnt = 0
for i in range(1,2021):
    for j in range(1,2021):
        if gcd(i,j)==1:
            cnt+=1
print(cnt)