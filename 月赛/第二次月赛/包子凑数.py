n = eval(input())
node = []
ans = 1
for i in range(n):
    a = eval(input())
    node.append(a)
for j in node:
    ans*=(j-1)
ans1 = ans/len(node)
if ans1*10%10 ==0:
    print('{:.0f}'.format(ans1))
else:
    print('INF')
    