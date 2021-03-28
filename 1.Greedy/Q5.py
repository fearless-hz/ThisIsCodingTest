N,M = map(int,input().split())
k=list(map(int,input().split()))
cnt=0
for i in range(len(k)-1) :
    for j in range(i+1,len(k)):
        if k[i]!=k[j] : cnt+=1

print(cnt)