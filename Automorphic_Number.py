n=int(input())
m=n
s=n*n
temp=10
flag=0
while(n>0):
    r=s%temp
    if(m==r):
        flag=1
        break
    n=n/10
    temp=temp*10
if(flag==1):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')