def flag(n):
    if '0' in str(n):
        return False
    s1= ''.join((lambda x:(x.sort(),x)[1])(list(str(n))))
    s2 = s1[::-1]
    sum_ = eval(s2) - eval(s1)
    sum_ = ''.join((lambda x:(x.sort(),x)[1])(list(str(sum_))))
    if sum_ == s1:
        return True
    else:
        return False
def main():
    for i in range(100000,1000000):
        if flag(i):
            print(i)
main()





    
    

        