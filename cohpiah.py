import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    sab = 0
    for i in range (6):
        sab += abs(as_a[i] - as_b[i])
        
    sab = sab / 6

    return sab


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    #Tamanho médio das palavras
    #Soma do Tamanho das palavras / Numero total de palavras
    soma_tamanho = 0
    soma_palavras = 0
    soma_palavras_diferentes = 0
    soma_palavras_unicas = 0
    lista_texto=[]
    caracteres_sentenca = 0
    caracteres_frase=0
    qty_sentencas = 0
    frases_sentenca = 0
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        caracteres_sentenca = caracteres_sentenca + len(sentenca)
        qty_sentencas += 1
        frases = separa_frases(sentenca)
        
        for frase in frases:
            palavras = separa_palavras(frase)
            
            frases_sentenca += 1
            caracteres_frase += len(frase)
            for palavra in palavras:
                soma_tamanho = soma_tamanho + len(palavra)
                soma_palavras += 1
                lista_texto.append(palavra)
    
    wal = soma_tamanho / soma_palavras
    
    
    #TTR - Relação Type-Token: Número de palavras diferentes utilizadas em um texto
    #divididas pelo total de palavras
    soma_palavras_diferentes = n_palavras_diferentes(lista_texto)
    ttr = soma_palavras_diferentes / soma_palavras

    #HLR - Razão Hapax Legomana é o número de palavras que aparecem uma única vez
    #dividido pelo total de palavras.
    soma_palavras_unicas = n_palavras_unicas(lista_texto)
    hlr = soma_palavras_unicas / soma_palavras

    # SAL Tamanho médio de sentença: Média simples do número de caracteres por sentença.
    sal = caracteres_sentenca / qty_sentencas

    # SAC Complexidade de sentença: Média simples do número de frases por sentença.
    sac = frases_sentenca / qty_sentencas

    # PAL Tamanho médio de frase: Média simples do número de caracteres por frase.
    pal = caracteres_frase / frases_sentenca
    
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    sab = []
    
    for texto in textos:
        assinatura = calcula_assinatura(texto)
        sab.append(compara_assinatura(ass_cp, assinatura))

    infectado = sab[0]
    indice = 0
            
    for item in range(len(sab)):
       if (sab[item]<= infectado):
           infectado = sab[item]
           indice = item + 1
    return indice
           


def main():

    assinatura_lida = le_assinatura()
    texto_lido = le_textos()
       
    provavel_infectado = avalia_textos(texto_lido, assinatura_lida)
    
    print("O autor do texto", provavel_infectado, "está infectado com COH-PIAH")
    
main()   
