# n elevado a k
def main():
    pot = 1
    i = 0
    n = int(input("Digite um numero inteiro n:"))
    k = int(input("Digite um numero inteiro k:"))
    while i < k:
        pot = pot * n
        i = i + 1
    print("O valor de", n, "elevado a", k, "eh igual a", pot)


if __name__ == "__main__":
    main()
