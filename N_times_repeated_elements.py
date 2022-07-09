n=int(input())
a=list(map(int,input().split()))
k=int(input())
flag=0
for i in range(n+1):
    if a.count(i)==k:
        print(i,end=' ')
        flag=1
if(flag==0):
    print('-1')
