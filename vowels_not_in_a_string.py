s=input()
a=s.lower()
c='aeiou'
l=[]
flag=0
for i in a:
    if i in c:
        l.append(i)
for i in c:
    if i not in l:
        print(i,end=' ')
        flag=1
if flag==0:
    print('0')
