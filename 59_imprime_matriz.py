def imprime_matriz(matriz):
    for linha in matriz:
        for coluna in range(len(linha)):
            if coluna==len(linha)-1:
                print(linha[coluna])
            else:
                print(linha[coluna], end = " ")
        

