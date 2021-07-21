
def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            return False
    return True

def selecao_direta(lista):
    fim = len(lista)

    for i in range(fim -1):
        # Inicialmente, o menor elemento já visto é o i-ésimo
        posicao_do_minimo = i

        for j in range(i+1, fim):
            if lista[j] < lista[posicao_do_minimo]:
                posicao_do_minimo = j
        lista[posicao_do_minimo], lista[i] = lista[i], lista[posicao_do_minimo]
    return lista



def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista) - 1
    if esta_ordenada(lista):
        
        while (primeiro <= ultimo):
            meio = (primeiro + ultimo) // 2
            print(meio)
            if lista[meio] == elemento:
                return meio
            else:
                if elemento < lista[meio]:
                    ultimo = meio -1
                else:
                    primeiro = meio+ 1
        return False
    else:
        selecao_direta(lista)
        busca(lista, elemento)
        


