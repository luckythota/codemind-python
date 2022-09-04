s=input()
v=s.split(" ")
n=[]
for i in v:
    n.append(i[::-1])
print(*n)
