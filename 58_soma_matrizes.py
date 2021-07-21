def soma_matrizes(m1, m2):

    if (len(m1) == len(m2)) and (len(m1[0])==len(m2[0])):
        soma = []
        for linha in range(len(m1)):
            soma_linha = []
            for coluna in range(len(m1[linha])):
                
                soma_linha.append(m1[linha][coluna] + m2[linha][coluna])
            soma.append(soma_linha)
        return soma
    else:
        return False
                    
