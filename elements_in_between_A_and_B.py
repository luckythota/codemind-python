n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
flag=0
for i in range(0,n):
    if a[i]>=b and a[i]<=c:
        print(a[i],end=' ')
        flag=1
if flag==0:
    print('-1')
        