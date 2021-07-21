
repeticao = 0
n=int(input("Digite o valor de n (n>0): "))
novon=n
if(n <= 0):
    print("Valor de n invalido")
        
else:
    d=int(input("Digite o valor de d (0<=d<=9): "))
    if (d < 0 or d > 9):
        print("Valor de d invalido")
    else:
            
        while(novon != 0 ):
        
            if ((novon%10) == d):
                repeticao = repeticao+1
            novon= novon//10
    
        print(" O digito",d,"ocorre",repeticao,"vezes em", n)

