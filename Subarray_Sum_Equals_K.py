n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    sum=0
    for j in range(i,n):
        sum+=a[j]
        if sum==k:
            c+=1
print(c)