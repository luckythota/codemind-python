a=input().lower()
b=input().lower()
s=a.split(" ")
t=b.split(" ")
c=0
for i in s:
    if i in t:
        if s.count(i)==t.count(i):
            c+=1
print(c)