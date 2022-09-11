s=input()
chr=input()
flag=0
for i in s:
    if chr in s:
        flag=1
        v=s.index(chr)
if flag==1:
    print('True')
    print(v)
else:
    print('False')