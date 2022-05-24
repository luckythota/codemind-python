n=int(input())
m=n
g=n
count=0
sum=0
while(m>0):
    r=m%10
    count=count+1
    m=m//10
while(g>0):
    d=g%10
    sum=sum+d**count
    count=count-1
    g=g//10
if(sum==n):
    print('True')
else:
    print('False')
    
    