n=int(input())
a=list(map(int,input().split()))
b,flag=0,0
for i in a:
    if a.count(i)==1:
        b=i
        print(b,end=' ')
        flag=1
if(flag==0):
    print('-1')
        