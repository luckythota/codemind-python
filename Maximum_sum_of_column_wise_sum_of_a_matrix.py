m,n=map(int,input().split())
b=[]
l=[]
for i in range(0,m):
    a=list(map(int,input().split()))
    b.append(a)
for i in range(0,n):
    sum=0
    for j in range(0,m):
        sum=sum+b[j][i]
        l.append(sum)
print(max(l))
        