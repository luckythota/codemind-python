a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
d=0
if a[0]>b[0]:
    c=c+1
elif b[0]>a[0]:
    d=d+1
if(a[1]>b[1]):
    c=c+1
elif(a[1]<b[1]):
    d=d+1
if(a[2])>b[2]:
    c=c+1
elif(a[2]<b[2]):
    d=d+1
print(c,d)