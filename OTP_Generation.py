s=input()
for i in s:
    if int(i)%2==0:
        continue
    else:
        v=int(i)*int(i)
        print(v,end='')
