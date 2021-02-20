lis = [[0 for i in range(100)] for j in range(100)]

num = 1  # 记录当前的数
for i in range(1,101):  # 层数
    for j, k in zip(list(range(i)), list(range(num, num + i))):
        if i % 2 == 0:  # 偶数层
            lis[j][i-j-1] = k
        else:
            lis[i-j-1][j] = k
        num += 1

print(lis[19][19])