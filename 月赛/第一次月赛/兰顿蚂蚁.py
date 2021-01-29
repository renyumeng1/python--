m,n = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(m)]
tr = [x for x in input().split()]
x,y,s,k = eval(tr[0]),eval(tr[1]),tr[2],eval(tr[3])
def move(x,y,s,step):
    if step == k:
        print(x,y)
        return
    if box[x][y]==0:
        box[x][y]=1
        if s =='U':
            return move(x,y-1,'L',step+1)
        if s=='D':
            return move(x,y+1,'R',step+1)
        if s=='L':
            return move(x+1,y,'D',step+1)
        if s=='R':
            return move(x-1,y,'U',step+1)
    else:
        box[x][y]=0
        if s=='U':
            return move(x,y+1,'R',step+1)
        if s=='D':
            return move(x,y-1,'L',step+1)
        if s=='L':
            return move(x-1,y,'U',step+1)
        if s=='R':
            return move(x+1,y,'D',step+1)
move(x,y,s,0)

            
