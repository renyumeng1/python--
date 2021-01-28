def func(n):
    if (n%4==0 and n%100!=0) or n%400 == 0:
        print('yes')
    else:
        print('no')
func(eval(input()))