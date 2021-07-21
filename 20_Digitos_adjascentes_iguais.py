# Verifica se o número digitado possui dois números consecutivos iguais.


def main():
    ant = 0
    flag = False
    num = int(input("Digite o numero inteiro: "))
    if num > 0:
        while num > 0:
            unid = num % 10
            num = num // 10
            if ant == unid:
                flag = True
                ant = unid
        
            else:
                ant = unid
    else:
        print("O número precisa ser maior que zero")

    if flag:
        print(" SIM. O número tem dois ou mais números consecutivos iguais.")
    else:
        print("Não. O número digitado não tem dois números adjascentes.")


main()
