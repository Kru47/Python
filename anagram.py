num=int(input())
output=[]

for i in range(num):
    count1=0
    count2=0
    First=input()
    Second=input()
    c=list(First)
    d=list(Second)
    for j in range(0,len(First)):
         if c[j] in d:
              count1=count1
         else:
              count1=count1+1
    for k in range(0,len(Second)):
         if d[k] in c:
              count2=count2
         else:
              count2=count2+1
    output.append(count1+count2)

for i in range(0,len(output)):
     print(output[i])