
n=int(input())
i=1
sum=0
for i in range(i,n,1):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print('True')
else:
    print("False")
        
