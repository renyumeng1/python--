def fi(n):
    def helper(n):
        if n<=2:
            return 1
        if n in memo:
            return memo[n]
        memo[n]=fi(n-1)+fi(n-2)
        return memo[n]
    memo = {}
    return helper(n)
print(fi(20))