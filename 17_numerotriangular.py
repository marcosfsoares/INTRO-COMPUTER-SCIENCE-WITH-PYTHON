# O número é triangular se é divisível por 4, 5 e 6.
def main():
    n = int(input("Digite um numero inteiro: "))
    if (n % 4 == 0) and (n % 5 == 0) and (n % 6 == 0):
        print(" O numero", n, "eh triangular")
    else:
        print("Numero nao triangular")


main()
