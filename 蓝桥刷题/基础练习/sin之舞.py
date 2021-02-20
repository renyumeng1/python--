n = eval(input())
def fir(n, ans=None):
    if ans == None:
        ans=[]
    for i in range(1,n+1):
        ans.append('sin')
        ans.append('(')
        ans.append(str(i))
        if i%2!=0:
            ans.append('-')
        elif i%2==0:
            ans.append('+')
    ans.pop()
    for i in range(1,n+1):
        ans.append(')')
    s1=''
    for i in ans:
        s1+=i
    return s1
s2 = ''
for i in range(1,n+1):
    if i==1:
        for j in range(n-1):
            s2+='('
    s2+=fir(i)
    s2+='+'
    s2+=str(n-i+1)
    if i<n:
        s2+=')'
print(s2)
        
    
