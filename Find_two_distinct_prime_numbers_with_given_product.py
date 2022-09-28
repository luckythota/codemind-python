n=int(input())
l=[]
k=[]
flag=0
for i in range(2,n):
    for j in range(2,n):
        if i!=j and j!=i:
            if n==i*j:
                l.append(i)
                l.append(j)
                flag=1
                break
for i in l:
    if i not in k:
        k.append(i)
if flag==1:
    print(*k)
else:
    print('-1')

            