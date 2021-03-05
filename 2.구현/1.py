N = int(input())
data = list(input().split())
x,y=1,1
dx=[0,-1,0,1] #열 : 동, 북, 서, 남
dy=[1,0,-1,0] #행

for i in data :
    if i=='R' and 1<=y<N : y+=1
    elif i=='L' and 1<y<=N : y-=1
    elif i=='U' and 1<x<=N : x-=1
    elif i=='D' and 1<=x<N : x+=1

print(x,y)