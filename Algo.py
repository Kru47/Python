def count_sb(n):
    output=0
    while(n):
        n=n & (n-1)
        output= output+1
    return output

Num=int(input())
print(count_sb(Num))