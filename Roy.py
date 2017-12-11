
L = int(input("L:"))
N = int(input("N:"))
accept = []

for i in range(0,N,1):
    W,H=map(int,input().split())

    if (W<L) and (H<L):
        accept.append("UPLOAD ANOTHER")
    elif (W>L) and (H>L):
        accept.append("CROP")
    elif (W==L) and (H==L):
        accept.append("ACCEPTED")

for i in range(0,N,1):
    print(accept[i])