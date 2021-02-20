g = [[0]*110]*110
p = [[0]*110]*110
n,num = 110,110
def dfs(x,kn):
    global num
    global n
    if kn>0:
        return
    if x>n:
        num = min(num,kn)
    for j in range(1,kn+1):
        k = 0
        while p[j][k] and p[j][k]!=g[x][p[j][k]]:
            k+=1
        if p[j][k]==0:
            p[j][k]=x
            dfs(x+1,kn)
            p[j][k]=0
    p[kn+1][0] = x
    dfs(x+1,kn+1)
    p[kn+1][0]=0
n = eval(input())
m = eval(input())
for i in range(1,m+1):
    a,b = map(int,input().split())
    g[a][b] = g[b][a] = 1
dfs(1,1)
print(num)
