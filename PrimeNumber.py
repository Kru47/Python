number = int(input())
check = "P"
output = [2]

for factor in range(2,number):
    for ifactor in range(2,factor):
        if factor%ifactor==0:
            check = "N"
            break
        else:
            check = "Y"
    if check is "Y":
        output.append(factor)

print(' '.join(map(str, output)))