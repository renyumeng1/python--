def flag(n):
    f = int(str(n)[0])
    s = int(str(n)[1])
    t = int(str(n)[2])
    if f**3+s**3+t**3 == n:
        return True
    return False
for i in range(100,1000):
    if flag(i):
        print(i)
    