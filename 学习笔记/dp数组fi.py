def new_func():
    def fib(n):
        dp = [0 for _ in range(n+1)]
        if n ==1:
            return n
        else:
            dp[1]=dp[2]=1
            for i in range(3,n+1):
                dp[i]=dp[i-1]+dp[i-2]
            return dp[n]
    n = eval(input())
    print('{:.0f}'.format(fib(n)%10007))

def fib(n):
    if n<=2:
        return 1
    prev = 1
    curr = 1
    for i in range(3,n+1):
        prev,curr = curr,prev+curr
    return curr
n = eval(input())
print(fib(n))