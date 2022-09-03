s=input()
flag=0
s=s.lower()
for i in range(0,len(s)//2):
    if(s[i]!=s[len(s)-i-1]):
        flag=1
        break
if(flag==0):
    print('True')
else:
    print('False')
    