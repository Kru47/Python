import math
def sumofsquares(n):
    i = n-1
    j = 1
    while(i != j and i>0):
        root1 = math.sqrt(i)
        root2 = math.sqrt(j)
        if int(root1 + 0.5) ** 2 == i and int(root2 + 0.5)**2 == j:
            if i + j == n:
                return "True"
        i = i-1
        j = j+1
    return "False"

def wellbracketed(st):
    count = 0
    for i in range(len(st)):
        if st[i] == "(":
            count+=1
        if st[i] == ")":
            count-=1
    if count==0:
        return "True"
    else:
        return "False"



def rotatelist(l,k):
    for i in range(k):
        m=l.pop(len(l)-1)
        l.insert(0,m)
    return l
