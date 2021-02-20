from math import sqrt
a,b,c = map(int,input().split())
delt = b**2-4*a*c
if delt < 0:
    print('NO')
elif delt ==0:
    if len(str((-b+sqrt(delt))/2*a))==3 and str((-b+sqrt(delt))/2*a)[2] == '0':
        print(int((-b+sqrt(delt))/2*a))
    else:
        print((-b+sqrt(delt))/2*a)
else:
    if len(str((-b+sqrt(delt))/2*a))==3 and str((-b+sqrt(delt))/2*a)[2] == '0':
        print(int((-b+sqrt(delt))/2*a),end = ' ')
        print(int((-b-sqrt(delt))/2*a))
    else:
        print((-b+sqrt(delt))/2*a,end = ' ')
        print((-b-sqrt(delt))/2*a)
