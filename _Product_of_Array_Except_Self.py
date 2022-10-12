n=int(input())
a=list(map(int,input().split()))
pro=1
for i in range(0,n):
    pro=pro*a[i]
for i in range(0,n):
    print(pro//a[i],end=' ')