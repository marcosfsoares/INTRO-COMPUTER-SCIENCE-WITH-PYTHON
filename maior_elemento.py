def maior_elemento(lista):
    n=lista[0]
    for numero in lista:
        if numero >= n:
            n=numero
    return n
