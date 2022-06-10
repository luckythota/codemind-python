t=int(input())
for i in range(1,t+1):
    n=int(input())
    m=n
    flag=0
    for j in range(1,m+1):
        if(m==j*j):
            flag=1
    if(flag==1):
        print('True')
    else:
        print('False')