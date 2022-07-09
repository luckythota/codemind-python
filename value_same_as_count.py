n=int(input())
a=list(map(int,input().split()))
d=0
for i in range(1,n+1):
    if a.count(i)==i:
        d+=1
print(d)