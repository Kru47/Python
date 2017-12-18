NofArrayElem, NoOfQuery = map(int, input().split())
InArray = []
InArray = list(map(int, input().split()))
OutArray = []
for i in range(0, NoOfQuery, 1):
    QueryNum, X, Y = map(int, input().split())
    if QueryNum == 1:
        InArray[X] = Y
    if QueryNum == 2:
        if X >= 0 and Y < NofArrayElem:
            OutArray.append(sum(InArray[X:Y+1]))
        else:
            OutArray.append(-1)

for j in range(len(OutArray)):
    print(OutArray[j])

        



