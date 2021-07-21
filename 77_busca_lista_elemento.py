def busca(lista, elemento):
    '''Busca elemento na lista e devolve o indice'''

    for pos, numero in enumerate(lista):
        if numero == elemento:
            return pos
    return False
