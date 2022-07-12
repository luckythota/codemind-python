n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
sum=0
for i in range(0,n):
    if a[i]>=b and a[i]<=c:
        sum=sum+a[i]
print(sum)
    