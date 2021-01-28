from itertools import permutations
x = [1,2,3,4,5,6,7,8,9]
ans = list(permutations(x))
count = 0
def flag(n):
    ans1 = n[0]+n[1]+n[3]+n[5]
    ans2 = n[0]+n[2]+n[4]+n[8]
    ans3 = n[5]+n[6]+n[7]+n[8]
    if ans1==ans2==ans3:
        return True
    return False
for i in ans:
    if flag(i):
        count+=1
print(count/6) #除去旋转和镜像的有2*3次
