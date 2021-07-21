# Escreva o seu programa aqui
def main():
    ant=0
    decrescente=0
    n=int(input("Digite a quantidade de numeros da sequencia: "))
    while(n>0):
        num=int(input("Digite o numero da sequencia: "))
        n=n-1
        if (num>=0):
                 
            if (num>=ant):
                ant=num
                crescente=True
            else:
                decrescente=decrescente+1
                ant=num
        else:
            if (ant==0):
                if(num<ant):
                    crescente=True
                    ant=num
                else:
                    decrescente=decrescente+1
                    ant=num
            else:
                if (num>=ant):
                    ant=num
                    crescente=True
            
                else:
                    decrescente=decrescente+1
                    ant=num
            
    if(crescente==True and decrescente==0):
        print("Esta em ordem crescente")
    elif (crescente ==False and decrescente==0):
        print("Erro Fatal")
    else:
        print("Nao esta em ordem crescente")
main()
        
