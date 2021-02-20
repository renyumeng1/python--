n = eval(input())
box = [eval(x) for x in input().split()]
def flag(lst):
    for i in range(len(lst)-1):
        if lst[i]!=lst[i+1]:
            return 1
    return 0
res = 0
while flag(box):
    fir = box[0]
    for i in range(len(box)):
        if i==len(box)-1:
            box[i] = box[i]/2+fir/2
        else:
            box[i] = box[i]/2+box[i+1]/2
    for i in range(len(box)):
        if box[i]%2!=0:
            box[i]+=1
            res +=1
print(res)
            
        