N=int(input())
K=list(map(int,input().split()))
result=0
mem=0
K=sorted(K)
for i in K :
    mem+=1
    if mem>=i :
        result+=1
        mem=0
print(result)
