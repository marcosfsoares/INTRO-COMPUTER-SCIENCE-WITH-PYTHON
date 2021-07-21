# Saber se os números da sequência de três estão em ordem crescente
def main():
    x1 = int(input("Digite o primeiro número inteiro: "))
    x2 = int(input("Digite o segundo número inteiro: "))
    x3 = int(input("Digite o terceiro número inteiro: "))

    if (x1 <= x2) and (x2 <= x3):
        print("Está em ordem crescente")
    else:
        print("Não está em ordem crescente")


main()
