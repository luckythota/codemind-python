m=int(input())
n=int(input())
for i in range(m,n+1):
    t=len(str(i))
    n=i
    s=0
    while n:
        r=n%10
        n=n//10
        if r!=0 and i%r==0:
            s+=1
    if s==t:
        print(i,end=' ')