time = input().split('/')
lst = []
for i in range(len(time)):
    if i == 0:
        if eval('19'+time[i])>=1960 and time[i+1]!='00' and time[i+2]!='00':
            lst.append('19'+time[i]+'-'+time[i+1]+'-'+time[i+2])
        if 1960<=eval('20'+time[i])<=2059 and time[i+1]!='00' and time[i+2]!='00':
            lst.append('20'+time[i]+'-'+time[i+1]+'-'+time[i+2])
    elif i==2:
        if eval('19'+time[i])>=1960 and time[i-1]!='00' and time[i-2]!='00':
            lst.append('19'+time[i]+'-'+time[i-1]+'-'+time[i-2])
            lst.append('19'+time[i]+'-'+time[i-2]+'-'+time[i-1])
        if 1960<=eval('20'+time[i])<=2059 and time[i-1]!='00' and time[i-2]!='00': 
            lst.append('20'+time[i]+'-'+time[i-1]+'-'+time[i-2])
            lst.append('20'+time[i]+'-'+time[i-2]+'-'+time[i-1])
def isRN(n):
    res = int(n)
    if (res%4==0 and res%100!=0) or res%400==0:
        return True
    return False
res = []
for i in lst:
    if isRN(i[0:4]) and i[5:7] =='02':
        if i[8]=='0':
            res.append(i)
        elif int(i[8:]) > 29:
            continue
        else:
            res.append(i)
    elif not isRN(i[0:4]) and i[5:7] =='02':
        if i[8]=='0':
            res.append(i)
        elif int(i[8:]) > 28:
            continue
        else:
            res.append(i)
    elif i[5]!='0' and eval(i[5:7]) > 12:
        continue
    elif (i[5:7]=='04' or i[5:7]=='06' or i[5:7]=='09' or i[5:7]=='11'):
        if i[8]=='0':
            res.append(i)
        elif int(i[8:]) >30:
            continue
        else:
            res.append(i)
    elif i[5:7]=='01' or i[5:7]=='03' or i[5:7]=='05' or i[5:7]=='07' or i[5:7]=='08'or i[5:7]=='10'or i[5:7]=='12':
        if i[8]=='0':
            res.append(i)
        elif int(i[8:]) >31:
            continue
        else:
            res.append(i)
    else:
        res.append(i)
for j in sorted(list(set(res))):
    print(j)



    
    