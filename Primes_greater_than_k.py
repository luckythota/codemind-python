n=int(input())
a=list(map(int,input().split()))
k=int(input())
sum=0
for i in range(n):
    count=0
    m=a[i]
    for j in range(1,m+1):
        if a[i]%j==0:
            count=count+1
    if count==2 and a[i]>=k:
        sum=sum+1
print(sum)
