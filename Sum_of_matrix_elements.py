m=int(input())
n=int(input())
b=[]
sum=0
for i in range(m):
    a=list(map(int,input().split()))
    b.append(a)
for i in range(m):
    for j in range(n):
        sum=sum+b[i][j]
print(sum)