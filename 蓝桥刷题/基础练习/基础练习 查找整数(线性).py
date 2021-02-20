def new_func():
    n = eval(input())
    lst = [eval(x) for x in input().split()]
    num = eval(input())
    if num in lst:
        print(lst.index(num)+1)
    else:
        print(-1)
new_func()
