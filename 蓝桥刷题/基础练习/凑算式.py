from itertools import permutations
cnt = 0 
x = [i for i in range(1,10)]
a = list(permutations(x,9))
for i in a:
    if (i[0]+(i[1]/i[2])+((i[3]*100+i[4]*10+i[5])/(i[6]*100+i[7]*10+i[8])))==10:
        cnt+=1
print(cnt)