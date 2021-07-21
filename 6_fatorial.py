# Fatorial de n
def main():
    
    n = int(input("Digite o valor de n:"))
    a = n
    fat = 1
    while a > 0:
        fat = fat * a
        a = a-1
    print("O valor de", n, "fatorial eh igual a:", fat)


main()
