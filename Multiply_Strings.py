s,t=map(int,input().split())
l=[]
l.append(s)
l.append(t)
for i in range(2):
    print(l[i]*l[i+1])