N=input()
data=[]
sum=0

for i in N :
    if ord(i)>=65 : #if i.isalpha()
        data.append(i)
    else:
        sum+=int(i)

data="".join(sorted(data))
print(data+str(sum))