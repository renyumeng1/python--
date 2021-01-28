ans = 0
for i in range(1,19000):
    if i%2!=0 and i%5!=0 and i%19!=0:
        ans+=1
print(ans)
