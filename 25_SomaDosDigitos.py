def main():
    
    calc=0
    n=int(input("Digite um número inteiro: "))
    while (n>0):
        unidade= n%10
        n=n//10
        calc=calc+unidade
    print(calc)

main()
