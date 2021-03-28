s=input()
lis=[]

cnt=0
answer=''
for i in s :
    if i.isalpha()==False :
        cnt+=int(i)
    else : lis.append(i)
lis.sort()
if cnt!=0 :
    lis.append(str(cnt))
answer=''.join(lis)
print(answer)