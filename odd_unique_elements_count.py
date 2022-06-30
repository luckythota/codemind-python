n=int(input())
a=list(map(int,input().split()))
b=set(a)
c=list(b)
d=0
for i in range(len(c)):
    if(c[i]%2!=0):
        d=d+1
print(d)