m,n=map(int,input().split())
b=[]
l=[]
for i in range(0,m):
    a=list(map(int,input().split()))
    l.append(sum(a))
    b.append(a)
for i in range(0,m):
    sum=0
    for j in range(0,n):
        sum=sum+b[i][j]
        l.append(sum)
for i in range(0,n):
    sum1=0
    for j in range(0,m):
        sum1=sum1+b[j][i]
        l.append(sum1)
print(max(l))