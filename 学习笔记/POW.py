def POW(x,n):
    if n == 1:
        return x
    else:
        return x*POW(x,n-1)
print(POW(10,3))