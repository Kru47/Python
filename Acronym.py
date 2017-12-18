DislikeW = int(input())
DisLikeList = []
output = []
for i in range(DislikeW):
    DisLikeList.append(input())

InputLen = int(input())
InputString = list(map(str, input().split(" ")))

for j in range(InputLen):
    if InputString[j] not in DisLikeList:
        output.append(InputString[j][0].upper())

str1 = '.'.join(output)

print(str1,)