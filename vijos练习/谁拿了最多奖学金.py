def get_price(name,grade,j_grade,work,student,paper):
    price = 0
    if grade > 80 and paper >= 1:
        price+=8000
    if grade > 85 and j_grade > 80:
        price+=4000
    if grade > 90:
        price+=2000
    if grade > 85 and student == 'Y':
        price+=1000
    if j_grade > 80 and work == 'Y':
        price+=850
    return list((price,name))
num = eval(input())
lst = []
lst_mess = [list(map(str,input().split())) for x in range(num)]
for i in range(num):
    lst.append(get_price(lst_mess[i][0],eval(lst_mess[i][1]),eval(lst_mess[i][2]),lst_mess[i][3],lst_mess[i][4],eval(lst_mess[i][5])))
max_num = 0
name_max = ''
for i in range(len(lst)):
    if lst[i][0] > max_num:
        max_num = lst[i][0]
        name_max = lst[i][1]
sum = 0
for i in range(num):
    sum+=lst[i][0]
print(name_max)
print(max_num)
print(sum)