N = int(input())
lis=list(map(int,input().split()))
lis.sort()
M = int(input())
lis2=list(map(int,input().split()))

def binary_search(array,target,start,end):
    while start<=end :
        mid = (start+end)//2
        if array[mid]==target :
            return mid
        elif array[mid]>target :
            end=mid-1
        else :
            start = mid+1
    return None
for i in lis2 :
    result = binary_search(lis,i,0,N-1)
    if result!=None :
        print('yes',end=' ')
    else :
        print('no', end=' ')
