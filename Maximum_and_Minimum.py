n=int(input())
a=list(map(int,input().split()))
l=[]
flag=0
for i in range(1,n+1):
    if a.count(i)==i:
        l.append(i)
        flag=1
if(flag==1):
    print(min(l),max(l),end=' ')
if(flag==0):
    print('-1')