def ordenada(lista) -> bool:
    '''Verifica se a lista está ordenada'''
    ordem = True
    crescente = False
    for numero in range(len(lista)-1):
        
        if lista[numero]<=lista[numero+1] and ordem:
            crescente = True
            
        elif lista[numero]>=lista[numero+1] and not crescente:
            ordem = False
        else:
                      
            return False
    return True
            
