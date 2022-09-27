s=input()
v=list(s.lower())
c=0
for i in v:
    if v.count(i)==1 and i!=' ':
        c+=1
print(c)
    