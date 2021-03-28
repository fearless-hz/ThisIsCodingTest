N=int(input())
cnt=0
cnt2=0

for i in range(len(str(N))//2):
    cnt+=int(str(N)[i])
for j in range(len(str(N))//2,len(str(N))):
    cnt2+=int(str(N)[j])

if cnt==cnt2 :
    print("LUCKY")
else :
    print("READY")