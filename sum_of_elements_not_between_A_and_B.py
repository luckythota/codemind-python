n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
flag=0
sum=0
for i in range(0,n):
    if a[i]>=b and a[i]<=c:
        flag=1
    else:
        sum=sum+a[i]
print(sum)