s=input()
v=list(s.lower())
flag=0
for i in v:
    if v.count(i)==1:
        print(i)
        flag=1
        break
if flag==0:
    print('-1')
    
    
    