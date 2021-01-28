#这是一道数学题，用到了数论的知识
#ax+by=C 无解的最大值C=ab-a-b
#能使他无解的数目为(a-1)(b-1)/2
a,b = map(int,input().split())
print(a*b-a-b)