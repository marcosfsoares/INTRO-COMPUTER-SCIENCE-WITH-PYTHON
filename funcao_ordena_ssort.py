def ordena(lista):

    tamanho = len(lista)

    for numero in range(tamanho - 1):
        minimo = numero
        for rapido in range(numero+1, tamanho):
            if lista[rapido] < lista[minimo]:
                minimo = rapido

        lista[numero], lista[minimo] = lista[minimo], lista[numero]
    return lista
                
            
