def inserts(A):
    for i in range(0,len(A)):
        for j in range(0,i,1):
            if A[i] < A[j]:
                A[i],A[j]=A[j],A[i]
    return A

L=[9,5,8,3,2,1]
print(inserts(L))


