n=int(input())
a=list(map(int,input().split()))
sum=0
c=0
flag=0
d=0
for i in range(1,n+1):
    if a.count(i)==i:
        c+=1
        sum=sum+i
        flag=1
        d=sum/c
if(flag==1):
    print('%.2f' %d)
else:
    print('-1')