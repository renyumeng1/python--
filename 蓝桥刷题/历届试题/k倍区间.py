n,k = map(int,input().split())
lst,s = [0],[0 for x in range(k)]
flag = [0]
res = 0
for i in range(1,n+1):
    lst.append(eval(input()))
    flag.append((flag[i-1]+lst[i])%k)
    s[flag[i]]+=1
for i in range(len(s)):
    res+=s[i]*(s[i]-1)//2
print(res+s[0])