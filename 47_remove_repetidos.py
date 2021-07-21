def remove_repetidos(lista):
    lista.sort()
    print(lista)
    a=0
    for n in range(len(lista)):
        
        if lista[a-1]==lista[a]:
            del lista[a-1]
        else:
            a=a+1
                
    return lista
