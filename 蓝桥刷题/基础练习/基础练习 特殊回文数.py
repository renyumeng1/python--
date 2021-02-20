def over_time():#超时
    n = eval(input())
    for i in range(10000,1000000):
        sum = 0
        for j in str(i):
            sum+=int(j)
        if sum == n and str(i) == str(i)[::-1]:
            print(i)


n = eval(input())
for i in range(10000,1000000):
    num = str(i)
    if num == num[::-1]:#用一层if减少了无用循环（先判断是不是回文数）
        if n == sum(int(j) for j in num):
            print(i)

