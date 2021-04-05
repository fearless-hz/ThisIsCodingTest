N = int(input())
array = list(map(int,input().split()))
start=0
end = len(array)
while start<=end :
    mid = (start+end)//2
    if array[mid]==mid :
        print(mid)
        break
    elif array[mid]>mid :
        end = mid-1
    else :
        start = mid+1
    print(-1)
    break