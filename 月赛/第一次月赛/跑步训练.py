ans = 0
flag = 10000
while True:
    flag-=600
    if flag<0:
        break
    flag+=300
    ans+=2
print(ans*60+(flag+600)*60/600)
        
    