for i in range(100,1000):
    sum = pow(i%10,3) + pow(i//10%10,3) + pow(i//100,3)
    if sum ==i:
        print(i)