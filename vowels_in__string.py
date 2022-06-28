s=input()
a=[]
flag=0
for i in s:
    if i in 'aeiouAEIOU':
        if i not in a:
            a.append(i)
        flag=1
if(flag==1):
    print(*a)
else:
    print('-1')