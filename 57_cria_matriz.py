def cria_matriz(num_linhas, num_colunas, valor):
    '''(int, int, valor) -> matriz(lista de listas)
    Cria e retorna uma matriz com linhas e colunas
    em que cada elemento é igual ao valor dado
    '''

    matriz = [] #lista vazia
    for i in range(num_linhas):
        #cria a linha i
        linha = [] # lista vazia
        for j in range(num_colunas):
            linha.append(valor)

        # adiciona lihna à matriz
        matriz.append(linha)
    return matriz


### método para mostrar matriz uma embaixo da outra

def mostra_matriz(matriz):

    '''for linha in matriz:
        for coluna in linha:
           
                print("{}".format(coluna), end="")
            
                #print(coluna, end=" ")
                #pass
                
        print()'''

    for linha in matriz:
        for coluna in range(len(linha)):
            if coluna==len(linha)-1:
                print(linha[coluna])
            else:
                print(linha[coluna], end = " ")
        
