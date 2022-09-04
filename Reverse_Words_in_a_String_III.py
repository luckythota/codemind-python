s=input()
v=s.split(" ")
l=[]
for i in v:
    l.append(i[::-1])
print(*l)