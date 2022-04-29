n=int(input())
i=1
flag=0
for i in range(i,n,1):
    if(n==i*(i+1)):
        flag=1
        break
if(flag==1):
    print('YES')
else:
    print("NO")