n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    c=0
    while(i!=0):
        r=i%10
        i=i//10
        c+=1
    b.append(c)
d=0
for i in b:
    if i%2==0:
        d+=1
print(d)