k = eval(input())
length = 5+4*k
box = [['.']*length for x in range(length)]
def cross(x,y,n):
    if n < 0:
        return
    len_ = 5 + 4 * n
    for i in range(y+2,len_-2):
        box[x][i] = box[x+len_-1][i] = '$'
    box[x+1][y+2] = '$'
    box[x+len_-2][y+2] = '$'
    box[x+1][y+len_-3] = '$'
    box[x+len_-2][y+len_-3]='$'
    
    box[x+2][y+2] = '$'
    box[x+2][y+len_-3] = '$'
    box[x+len_-3][y+2] = '$'
    box[x+len_-3][y+len_-3] = '$'
    
    box[x+len_-3][y+1] = '$'
    box[x+2][y+1] = '$'
    box[x+2][y+len_-2] = '$'
    box[x+len_-3][y+len_-2] = '$'
    for i in range(x+2,x+2+len_-4):
        box[i][y] = box[i][y+len_-1] = '$'
    return cross(x+2,y+2,n-1)
cross(0,0,k)
for i in range(length):
    for j in range(length):
        print(box[i][j],end = '')
    print()