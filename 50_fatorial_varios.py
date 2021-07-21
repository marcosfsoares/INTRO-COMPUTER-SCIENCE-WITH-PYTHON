def fatorial():
    numero=1
    numero_digitado=int(input("Digite o numero para transformar em fatorial: "))

    while(numero >0):
        fat=1
        numero=numero_digitado
        while(numero>=1):
            fat=fat*numero
            numero=numero-1
        print("O fatorial de",numero_digitado,"é igual a", fat)
        numero=numero_digitado=int(input("Digite o numero para transformar em fatorial: "))
fatorial()


        
