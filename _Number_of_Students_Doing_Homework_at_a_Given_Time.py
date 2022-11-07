m=int(input())
a=list(map(int,input().split()))
n=int(input())
b=list(map(int,input().split()))
q=int(input())
c=0
for i in range(0,m):
    if q>=a[i] and q<=b[i]:
        c+=1
        
print(c)
    