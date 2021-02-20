n,x = map(int,input().split())
cnt = 0
for i in range(1,n+1):
    if str(x) in str(i): 
        if i<=10:
            cnt+=1
        else:
            for j in str(i):
                if x == int(j):
                    cnt+=1
print(cnt) 