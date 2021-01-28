# s1 = input()
# s2 = input()

# count = []

# for i in range(len(s1)):
#     if s1[i]!=s2[i]:
#         count.append(i)
# ans = count[-1]
# for i in range(len(count)-1):
#     ans-=count[i]
# print(ans)

#上方有错

s1 = input()
s2 = input()
lst1 = [x for x in s1]
lst2 = [x for x in s2]
count = 0
for i in range(len(lst1)):
    if lst1[i]!=lst2[i]:
        if lst1[i]=='*':
            lst1[i]='o'
        else:
            lst1[i]=='*'
        if lst1[i+1]=='*':
            lst1[i+1]='o'
        else:
            lst1[i+1]='*'
        count+=1
    if lst1==lst2:
        break
print(count)        
    

