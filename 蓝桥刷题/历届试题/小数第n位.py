def new_func():#超时
    a,b,n = map(int,input().split())
    ans1 = str('{:.10000f}'.format(a/b))
    ans2 = ans1.index('.')
    ans3 = ans1[ans2+1:]
    if len(ans3[n-1:n-2+4]) == 1:
        print(int(ans3[n-1:n-2+4])*100)
    else:
        print(int(ans3[n-1:n-2+4]))

a,b,n=map(int,input().split())
a=a%b
while n>1000:  #小数后直接第1000位(大数据)
    a=a*(10**1000)
    n=n-1000 #举个例子，1/8=0.125;100/8=12.5 
    a=a%b    #1/8小数后第三位和100/8小数后第1位是    一样的
for i in range(n+2):
    a=a*10
    if i>=n-1:         
       print(a//b,end='')
    a=a%b

