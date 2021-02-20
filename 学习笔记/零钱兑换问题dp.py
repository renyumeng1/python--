def coinChange(coins,amount):
    def dp(n):
        if n == 0:return 0
        if n < 0:return -1
        res = float('inf')
        for coin in coins:
            subpro = dp(n-coin)
            if subpro ==-1:
                continue
            res = min(res,1+subpro)
        return res if res!= float('inf') else -1
    return dp(amount)
a = coinChange([1,2,5],11)
print(a)
        