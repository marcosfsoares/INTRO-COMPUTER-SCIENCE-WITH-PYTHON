# FizzBuzz se o número for divisível por 3 e por 5.
def main():
    x = int(input("Digite um número inteiro: "))
    if (x % 5 == 0) and (x % 3 == 0):
        print("FizzBuzz")
    else:
        print(x)


main()
