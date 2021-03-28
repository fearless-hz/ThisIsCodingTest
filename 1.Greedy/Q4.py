n=int(input())
lis=list(map(int,input().split()))
lis.sort()
result=1
for i in lis :
    if result<i :
        print(result)
        break
    result+=i

print(result)