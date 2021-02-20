x = []
cnt = 0
for line in (open("F:/python学习/月赛/第五次月赛/2020.txt")):
    x.append(line.strip())
m = len(x)
n = len(x[0])
for i in range(m):
    for j in range(n):
        if j<=n-4:
            if x[i][j]+x[i][j+1]+x[i][j+2]+x[i][j+3] =='2020':
                cnt+=1
        if i<=m-4:
            if x[i][j]+x[i+1][j]+x[i+2][j]+x[i+3][j] =='2020':
                cnt+=1
        if i<=m-4 and j<=n-4:
            if x[i][j]+x[i+1][j+1]+x[i+2][j+2]+x[i+3][j+3] =='2020':
                cnt+=1
print(cnt)