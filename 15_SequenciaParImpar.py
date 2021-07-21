def main():
    par = 0
    impar = 0
    n = int(input("Digite a quantidade de numeros na sequencia: "))
    while n > 0:
        seq = int(input("Digite o numero da sequencia: "))
        n = n - 1
        if seq % 2 == 0:
            print(seq, "eh par")
            par = par + 1
            
        else:
            print(seq, "eh impar")
            impar = impar + 1
            
    print("A sequencia tem", par, "numeros pares e", impar, "numeros impares")


main()
