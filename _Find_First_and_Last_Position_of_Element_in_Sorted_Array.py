n=int(input())
a=list(map(int,input().split()))
k=int(input())
flag=0
l=[]
for i in range(0,n):
    if a[i]==k:
        l.append(i)
        flag=1
if flag==1:
    print(min(l),max(l),end=' ')
else:
    print('-1 -1')