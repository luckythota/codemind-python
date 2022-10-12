n=int(input())
b=[]
sum=0
sum1=0
for i in range(0,n):
    a=list(map(int,input().split()))
    b.append(a)
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            sum+=b[i][j]
        if(j==(n-i)-1):
            sum1+=b[i][j]
print('Principal Diagonal:',end='')
print(sum)
print('Secondary Diagonal:',end='')
print(sum1)
