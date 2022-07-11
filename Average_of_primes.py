n=int(input())
a=list(map(int,input().split()))
count=0
sum=0
c=0
for i in range(n):
    count=0
    m=a[i]
    for j in range(1,m+1):
        if a[i]%j==0:
            count=count+1
    if count==2:
        sum=sum+a[i]
        c+=1
v=sum/c
print('%.2f' %v)