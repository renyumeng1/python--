num = 0
def Hanoi(n,x,y,z):
    global num
    if n==1:
        num+=1
        print("将第%d个盘片从%c移动到%c"%(n,x,z))
    else:
        Hanoi(n-1,x,z,y)
        num+=1
        print("将第%d个盘片从%c移动到%c"%(n,x,z))
        Hanoi(n-1,y,x,z)
Hanoi(3,'x','y','z')
print(num)