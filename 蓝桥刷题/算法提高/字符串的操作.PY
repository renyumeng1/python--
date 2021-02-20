def Append(S,s):
        for i in s:
                S.append(i)

def Insert(S,x,s):
        for i in range(len(s)):
                S.insert(x-1+i,s[i])

def Swap(S,a,b,c,d):
        n = len(S)
        if n > d:
                n1 = S[0:a-1]
                n2 = S[a-1:b]
                n3 = S[b:c-1]
                n4 = S[c-1:d]
                n5 = S[d:]
                S = n1+n4+n3+n2+n5
        elif n == d:
                n1 = S[0:a-1] 
                n2 = S[a-1:b]
                n3 = S[b:c-1]
                n4 = S[c-1:]
                S =  n1+n4+n3+n2
        return S

def Reverse(S,a,b):
        n = len(S)
        if a > 1:
                if b < n:
                        n1 = S[:a-1]
                        n2 = S[a-1:b]
                        n3 = S[b:]
                        S = n1 + n2[::-1] +n3
                elif b == n:
                        n1 = S[:a-1]
                        n2 = S[a-1:]
                        S = n1 + n2[::-1]
        else:
                if b < n:
                        n1 = S[:b]
                        n2 = S[b:]
                        s = n1[::-1] + n2
                else:
                        S = S[::-1]
        return S

def fun(S,nums):
        a = nums.split()
        if a[0] == 'Append':
                Append(S,a[1])
        elif a[0] == 'Insert':
                Insert(S,int(a[1]),a[2])
        elif a[0] == "Swap":
                S = Swap(S,int(a[1]),int(a[2]),int(a[3]),int(a[4]))
        elif a[0] == "Reverse":
                S = Reverse(S,int(a[1]),int(a[2]))
        return S

if __name__ == "__main__":
        S = list(input())
        n = int(input())
        if 1<=n<=150:
                while n > 0:
                        nums = input()
                        S = fun(S,nums)
                        n -= 1
        print(''.join(S))