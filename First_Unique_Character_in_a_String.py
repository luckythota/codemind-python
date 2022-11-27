s=input()
l=list(s)
flag=0
for i in l:
    if l.count(i)==1:
        k=l.index(i)
        flag=1
        break
if flag==1:
    print(k)
else:
    print('-1')
        
