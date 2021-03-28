N=int(input())
lis = list(map(int,input().split()))
cnt=0
group=0
lis.sort()
for i in range(len(lis)):
    group+=1
    if lis[i] == group :
        cnt+=1
        group=0

print(cnt)