# Dado n>0, Verifica quantas vezes ocorre o dígito "d" no número "n".
def main():

    repeticao = 0
    n = int(input("Digite o valor de n (n>0): "))
    d = int(input("Digite o valor de d (0<=d<=9): "))

    novon = n
    if d < 0 or d > 9:
        print("Valor de d invalido")
        novon = 0
        
    while novon != 0:
        # O resto da divisão por 10 verifica a unidade
        if novon % 10 == d:
            repeticao = repeticao + 1

        # É comparada a unidade com o dígito procurado e depois dividido por 10...
        novon = novon // 10
    if n <= 0:
        print("Valor de n invalido")
    else:
        print(" O digito", d, "ocorre", repeticao, "vezes em", n)


main()
