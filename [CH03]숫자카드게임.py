N,M=map(int,input().split())
result=0
for i in range(N):
    data = list(map(int,input().split()))
    min_ = min(data)
    result=max(result,min_)
    print(result)

print(result)