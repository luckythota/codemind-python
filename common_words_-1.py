s1=input()
s2=input()
x=s1.lower()
y=s2.lower()
a=x.split(" ")
b=y.split(" ")
c=0
for i in a:
    if i in b:
        c+=1
print(c)