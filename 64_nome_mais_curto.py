def nome_mais_curto(lista_de_nomes):
    '''Devolve o nome mais curto de uma lista de nomes'''
    #curto = [0]
    curto = 0
    lista_de_nomes = [nome.strip() for nome in lista_de_nomes]
    #curto = [lista_de_nomes.index(nome) for nome in lista_de_nomes if len(nome)<= len(lista_de_nomes[curto[-1]])]
    #curto = [item for item in range(1,len(lista_de_nomes)) if len(lista_de_nomes[item])<= len(lista_de_nomes[curto[-1]])]
    for item in range(1, len(lista_de_nomes)):
        if len(lista_de_nomes[item])< len(lista_de_nomes[curto]):
            curto = item
        else:
            pass
    
    
    #lista_de_nomes = [nome.capitalize() for nome in lista_de_nomes]
    #print("sinal")
    #print(lista_de_nomes)
    #print(curto)

    #return lista_de_nomes[curto[-1]].capitalize()
    return lista_de_nomes[curto].capitalize()


def testa_mais_curto():
    lista1 = ['Abzzzzzzzzzzzzzzzzzzz',
              'mariazzzzzzzzzzzzzzz',
              'Jequitinhonhaaaaaaaasasdas',
              'paasasasasas',
              'Isabelaasasasasa',
              'Joaasasasaasnaa',
              'Tsaasasasaasaamanduateí',
              'abacaxibacate',
              'Joasasasasasasaao'
              ]
    lista2 = ['Ab', 'maria', 'Jequitinhonha', 'pa ', ' Isabela ', 'Joana', 'Tamanduateí', 'abacaxibacate', 'Joao']

    if nome_mais_curto(lista1)=='Paasasasasas':
        
        print( "Passou com 'paasasasasas'")
    else:
        
        print( 10*"#", "ERRO!!! Devolveu {} como mais curto!".format(nome_mais_curto(lista1)), 10*"#")
    
    if nome_mais_curto(lista2)=='Ab':
               
        print( "Passou com 'Ab'")
    else:
        print( 10*"#", "ERRO!!! Devolveu {} como mais curto!".format(nome_mais_curto(lista2)), 10*"#")
    

