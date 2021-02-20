box = [eval(x) for x in input().split()]
ans = box[3]/box[0]+box[4]/box[1]+box[5]/box[2]
n = box[-1]
print('%.*f'%(n,ans))#需要保留到n位时使用正则表达式'%.*f'%(n,ans)