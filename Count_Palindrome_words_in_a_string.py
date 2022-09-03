def checkpalin(word):
    if word.lower()==word.lower()[::-1]:
        return True
def countpalin(str):
    count=0
    v=str.split(" ")
    for elements in v:
        if checkpalin(elements):
            count+=1
    print(count) 
str=input()
countpalin(str)
