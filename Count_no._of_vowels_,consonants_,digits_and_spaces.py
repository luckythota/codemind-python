s=input()
v=0
c=0
d=0
n=0
for i in s:
    if i in 'aeiouAEIOU':
        v=v+1
    if i in '0123456789':
        d=d+1
    if i in ' ':
        n=n+1
    if i in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
        c=c+1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',n)