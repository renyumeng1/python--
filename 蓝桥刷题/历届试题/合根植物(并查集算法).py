def find(x):
    p=x
    while x!=pre[x]:
        x = pre[x]
    return x
m,n = map(int,input().split())
cnt = m*n
pre = [x for x in range(m*n)]+[0]*100000
k = eval(input())
for i in range(k):
    a,b = map(int,input().split())
    aa = find(a)
    bb = find(b)
    if aa!=bb:
        pre[aa]=pre[bb]
        cnt-=1
print(cnt)

            
            
        
            
   