t=int(input())
for i in range(1,t+1):
    n=int(input())
    m=n
    sum=0
    while(n!=0):
        r=n%10
        n=n//10
        sum=sum*10+r
    if(sum==m):
        print('True')
    else:
        print('False')