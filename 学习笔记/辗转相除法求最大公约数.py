def gcd(a,b):
    x = max(a,b)
    y = min(a,b)
    r = x%y
    if r==0:
        return y
    else:
        while r!=0:
            x = y
            y = r
            r = x%y
        return y
print(gcd(6,15))