#求最小公倍数
#两个数的乘积=最大公因数*最小公倍数
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
        if r==0:
            r=1
        return y
d,e,f = map(int,input().split())
x1 = gcd(d,e)
x2 = gcd(e,f)
ans1 = d*e/x1
ans2 = e*f/x2
x3 = gcd(ans1,ans2)
print('{:.0f}'.format(ans1*ans2/x3))