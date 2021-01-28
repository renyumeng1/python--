#需要选几个就写几个循环
#并且第一次的循环次数为len(list)-(循环次数-1)次(后依次-1)
lst = [1,2,3,4,5,6,7,8,9]
len_ = len(lst)
#选四个
count = 0
for i in range(0,len_-3):
    for j in range(i+1,len_-2):
        for k in range(j+1,len_-1):
            for l in range(k+1,len_):
                count+=1
                print(lst[i],lst[j],lst[k],lst[l])
    print()
print(count)

#或者直接使用itertools中的 combinations

 