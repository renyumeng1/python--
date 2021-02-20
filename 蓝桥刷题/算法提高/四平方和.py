from math import sqrt
n = eval(input())
def mean(n):
    for i in range(int(sqrt(n))+1):
        for j in range(int(sqrt(n))+1):
            for k in range(int(sqrt(n))+1):
                for l in range(int(sqrt(n))+1):
                    if n==i**2+j**2+k**2+l**2:
                        print(i,end=" ")
                        print(j,end=" ")
                        print(k,end=" ")
                        print(l,end=" ")
                        return
mean(n)

