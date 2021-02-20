def flag(lst):
    cnt = 1
    if lst[0] > 0 and lst[0] == max(lst):
        return cnt
    elif lst[0] < 0 and lst[0] == max(lst):
        return cnt
    else:
        for i in lst:
            if lst[0] > 0:
                if lst[0]*i > 0 and lst[0] > i:
                    cnt += 1
                elif lst[0]*i < 0 and lst[0] < i:
                    cnt += 1
            elif lst[0] < 0:
                if lst[0]*i > 0 and lst[0] > i:
                    cnt += 1
                elif lst[0]*i < 0 and abs(lst[0]) > i:
                    cnt += 1
        return cnt
n = eval(input())
lst = [eval(x) for x in input().split()]
print(flag(lst))