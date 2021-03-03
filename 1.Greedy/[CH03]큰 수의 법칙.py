N,M,K=map(int,input().split())
data = list(map(int, input().split()))
result=0
cnt=0
err=0
data.sort(reverse=True)
while(cnt<M):
    result+=data[0]
    cnt+=1
    err+=1
    if err==K:
        result=result-data[0]+data[1]
        err=0


print(result)