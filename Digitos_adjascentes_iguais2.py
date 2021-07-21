cont=0

Flag = False
num=int(input("Digite o numero inteiro: "))
ant=num%10
while (num>0):
    num=num//10
    unid=num%10
    
    if (ant==unid):
        Flag = True
        ant=unid
    
    else:
        ant=unid
        

if (Flag):
    print("sim")
else:
    print("não")


