t=int(input())
seconds = []
for i in range(t):
    arr=[]
    N,K=map(int,input().split(' '))
    arr=list(map(int,input().split(' ')))
    arr.sort()
    if arr[0]>=K:
       seconds.append(0)
    else:
       seconds.append(K-arr[0])
       
for j in range(t):
    print(seconds[j])