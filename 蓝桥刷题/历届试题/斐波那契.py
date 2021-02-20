n,m,p = map(int,input().split())
def fib(n,sum):
    if n<=2:
        return 1
    x1=1
    x2=1
    if sum == 2:
        for i in range(3,n+1):
            x1,x2 = x2,x1+x2
            sum=sum+x2
        return sum
    else:
        for i in range(3,n+1):
            x1,x2 = x2,x1+x2
        return x2
print(fib(n,2)%fib(m,None)%p)
    