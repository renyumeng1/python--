def gcd(a,b):
    x = max(a,b)
    y = min(a,b)
    r = x%y
    if r == 0:
        return y
    else:
        while r!=0:
            x = y
            y = r
            r = x%y
        return y
if __name__ == 'main':
    count = 0
    for i in range(1,19000):
        if gcd(i,19000) == 1:
            count+=1
    print(count)