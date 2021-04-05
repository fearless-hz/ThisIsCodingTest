n,m = map(int,input().split())
array = list(map(int,input().split()))
end = max(array)
start=0
result=0

while start<=end :
    mid = (start+end)//2
    print(mid)
    lis2=[]
    for i in array :
        if i>=mid :
            lis2.append(i-mid)
    if sum(lis2)<m :
        end = mid-1
    else :
        result= mid
        start = mid+1
print(result)