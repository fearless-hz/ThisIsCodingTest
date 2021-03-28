s= input()
cnt=0 #0을1로
cnt2=0 #1을0으로
for i in range(len(s)-1) :
    if s[i] != s[i+1] and s[i]=='0':cnt+=1
    elif s[i]!= s[i+1] and s[i]=='1' :
        cnt2+=1

result=min(cnt,cnt2)
print(result)