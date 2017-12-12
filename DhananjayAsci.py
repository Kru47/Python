'''variable="="
print(ord(variable))
print(chr(67))'''


def is_prime (factor):

    for ifactor in range(2,factor):
        if factor%ifactor==0:
            check = "N"
            break
        else:
            check = "Y"
    if check is "Y":
        return 1
    else:
        return 0


#NumberOfIps = input("Enter N:")
NumberOfTimes= int(input(""))


Mega = []

for times in range(0, NumberOfTimes, 1):
    MaxL = int(input(""))
    DhString = input("")
    DHNew = []
    for i in range(0, MaxL):
        Asc = ord(DhString[i])
        #print(Asc)
        for j in range(Asc+1, 122, 1):
            if is_prime(j) is 1:
                Upper_Prime = j
                break
        for k in range(Asc-1, 0, -1):
            if is_prime(k) is 1:
                Lower_Prime = k
                break
        if Asc-Lower_Prime > Upper_Prime-Asc:
            DHNew.append(chr(Upper_Prime))
        elif Asc-Lower_Prime < Upper_Prime-Asc:
            DHNew.append(chr(Lower_Prime))
        else:
            DHNew.append(chr(Lower_Prime))
    Mega.append(DHNew)


for i in range(0, times+1 ,1):
    print(''.join(map(str, Mega[i])))





