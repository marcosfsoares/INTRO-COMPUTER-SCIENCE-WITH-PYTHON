# escreva o seu programa
def main():
    cont = 10
    repeticao = 0
    n=int(input("Digite o valor de n (n>0): "))
    d=int(input("Digite o valor de d (0<=d<=9): "))
    

    novon=n
    if (d < 0 or d > 9):
        Print("Valor de d invalido")
        novon = 0
        
    while(novon != 0 ):
        
        if ((novon%10) == d):
            repeticao = repeticao+1

        
        novon= novon//10
    if(n <= 0):
        print("Valor de n invalido")
    else:
        print(" O digito",d,"ocorre",repeticao,"vezes em", n)
main()
