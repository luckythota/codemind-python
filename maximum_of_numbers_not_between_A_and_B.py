n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
l=[]
flag=0
for i in range(0,n):
    if a[i]>=b and a[i]<=c:
        continue
    else:
        l.append(a[i])
        flag=1
if flag==1:
    print(max(l))
else:
    print('-1')
        