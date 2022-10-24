n=int(input())
a=list(map(int,input().split()))
k=int(input())
flag=0
for i in range(0,n):
    if a[i]==k:
        v=i
        flag=1
if flag==1:
    print(v)
else:
    print('-1')