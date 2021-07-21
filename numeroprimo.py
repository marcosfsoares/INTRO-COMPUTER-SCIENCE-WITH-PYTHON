
primo=False
n=int(input("Digite um número inteiro: "))
i=2
if(n==1 or n==2):
    primo=True
else:
    
    while(i<n and n>0):
    
        if((n%i)!=0):
            primo=True
            i=i+1
        elif(n==1):
            i=i+1
        else:
            primo=False
            i=n

if (primo and n>0):
    print("primo")
elif (not primo and n>0):
    print("não primo")
else:
    print("número menor ou igual a zero")



