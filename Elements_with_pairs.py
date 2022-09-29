n=int(input())
a=list(map(int,input().split()))
flag=0
for i in a:
    if len(a)%2==0:
        flag=1
    else:
        a.append(0)
if flag==1:
    print(*a)
else:
    print(*a)