
              
     
    
Stype=["WS","MS","AS","AS","MS","WS","WS","MS","AS","AS","MS","WS"]
Num=int(input("Enter n: "))
Sno=[]
TypeOfSeat=[]
for i in range(0,Num):
    SnoIp=int(input("Enter seat no: "))
    i=0
    j=12
    for chk in range(0,9,1):
       # print(i,j)
        if SnoIp>i and SnoIp<=j:
           if SnoIp<=12:
               if SnoIp<=(i+j)/2:
                 # print(12-SnoIp+1,Stype[-SnoIp])
                  Sno.append(12-SnoIp+1)
                  TypeOfSeat.append(Stype[-SnoIp])
               else:
                 # print(12%SnoIp+1,Stype[-SnoIp])
                  Sno.append(12%SnoIp+1)
                  TypeOfSeat.append(Stype[-SnoIp])
               break
           else:
               if SnoIp<=(i+j)/2:
                   res=SnoIp%i
                   N=j-res+1
               else:
                   res=SnoIp%i
                   N=j-res+1
              # print(N,Stype[-res])
               Sno.append(N)
               TypeOfSeat.append(Stype[-res])
               break
        i=i+12
        j=j+12
        
for i in range(0,Num):
     print(Sno[i]," ",TypeOfSeat[i])       

                   
               
   
