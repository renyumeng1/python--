def binarySearch(arr,l,r,x):
    if r>=l:
        mid = int(l + (r - l)/2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr,l,mid-1,x)
        else:
            return binarySearch(arr,mid+1,r,x)
    else:
        return -1
n = eval(input())
arr = [eval(x) for x in input().split()]
x = eval(input())
ans = binarySearch(arr,0,len(arr)-1,x)
if ans !=-1:
    print(ans+1)
else:
    print(ans)
