dividend = eval(input("Please enter the dividend:"))
divisor = eval(input("Please enter the divisor:"))
while divisor==0:
    divisor = eval(input("Error: divisor can not be zero! Please enter a new divisor:"))
print('{:.0f}'.format(dividend/divisor))