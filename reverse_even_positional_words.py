s=input()
v=s.split(" ")
for i in range(0,len(v),2):
    n=''
    for j in v[i]:
        n=j+n
    v[i]=n
rs=' '.join(v)
print(rs)

