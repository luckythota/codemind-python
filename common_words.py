s1=input()
s2=input()
v=s1.lower().split(" ")
n=s2.lower().split(" ")
l=[]
for i in n:
    if i in v:
        l.append(i)
print(*l)