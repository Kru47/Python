    num=int(input())
    output=[]

    for i in range(num):

        First, Second = map(str, input().split())
        c=list(First)
        d=list(Second)
        c.sort()
        d.sort()

        if len(c) == len(d):
            if c == d:
                output.append("YES")
            else:
                output.append("NO")
        else:
            output.append("NO")

    for i in range(0, len(output)):
        print(output[i])