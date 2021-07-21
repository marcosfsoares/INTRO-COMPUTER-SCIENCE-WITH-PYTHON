# Escreva o seu programa aqui
def main():
    cont=0
    ant=0
    Flag = False
    num=int(input("Digite o numero inteiro: "))
    if (num>0):
        while (num>0):
            unid=num%10
            num=num//10
            if (ant==unid):
                Flag = True
                ant=unid
        
            else:
                ant=unid
    else:
        print("O número precisa ser maior que zero")

    if (Flag):
        print(" A resposra é SIM")
    else:
        print("A resposta é NÃO")
main()
        
