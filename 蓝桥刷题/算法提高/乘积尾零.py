num = [eval(x) for x in input().split()]
cnt = 0
ans = 1
for i in range(len(num)):
    ans*=num[i]
    while ans%10==0:
        ans/=10
        cnt+=1
print(cnt)
    