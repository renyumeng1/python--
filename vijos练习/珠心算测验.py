n = eval(input())
num = [eval(x) for x in input().split()]
lst = []
#re_num = [num for num in range(n)]
count = 0
for i in num:
    for j in num:
        if i==j:
            continue
        else:
            sum=i+j
            if sum in lst:
                continue
            else:
                lst.append(sum)
                if sum in num:
                    count+=1
print(count)      
