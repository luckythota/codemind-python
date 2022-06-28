s=input()
count=0
c=0
a=[]
b=[]
for i in s:
    if i in 'aeiou':
        if i not in a:
            a.append(i)
            count=count+1
for i in s:
    if i in "AEIOU":
        if i not in b:
            b.append(i)
            c=c+1
if(count==5 or c==5):
    print("True")
else:
    print("False")