def counter(n):
    if n=='ADD':
        flag.append('add')
    if n=='SUB':
        flag.append('sub')
    if n=='MUL':
        flag.append('mul')
    if n=='DIV':
        flag.append('div')
    if n=='MOD':
        flag.append('mod')
    if n=='EQUAL':
        if flag[1]=='add':
            return flag[0]+flag[-1]
        if flag[1]=='sub':
            return flag[0]-flag[-1]
        if flag[1]=='mul':
            return flag[0]*flag[-1]
        if flag[1]=='div':
            return flag[0]/flag[-1]
        if flag[1]=='mod':
            return flag[0]%flag[-1]
def change_10(str(num),k):
    x = 0
    for i in range(0,len(num)):
        if num[i]>='0' and num[i]<='9':
            x = x*k+num[i]-'0'
        else:
            x = x*k+num[i]-'A'+10
    return x
def change_k (x,k):
    if x == 0:
        return '0'
    s = ''
    while(x):
        if x%k<10:
            s+=str(x%10)+'0'
        else:
            s+=str((x%k) - 10) + 'A'
        x/=k
    s = s.join((lambda:x(x.reverse,x)[1])(list(s)))
    return s
n = eval(input())
node = []
flag = [0]
k = 10
while n:
    n-=1
    s = input()
    node.append(s)
for i in node:
    counter(i)
    if i[0:3] == 'NUM':
        flag.append(eval(i[4:]))
    elif i == 'CLEAR':
        flag.pop()
    elif i[0:6] == 'CHANGE':
        k = eval(i[7:])
        
    
    
        
    
    
        
