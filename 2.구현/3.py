N=input()
#8*8 (a~h / 1~8)
cnt=0
dx=[2,2,-2,-2,1,1,-1,-1]
dy=[-1,1,-1,1,-2,2,-2,2]

for i in range(8):
    x=ord(N[0])+dx[i]
    y=int(N[1])+int(dy[i])
    if y>=1 and y<=8 and x>=97 and x<=104:
        cnt+=1
print(cnt)