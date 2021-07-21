def menor_nome(lista_de_nomes):
    '''Devolve o nome mais curto de uma lista de nomes'''

    curto = 0
    lista_de_nomes = [nome.strip() for nome in lista_de_nomes]

    for item in range(1, len(lista_de_nomes)):
        if len(lista_de_nomes[item]) < len(lista_de_nomes[curto]):
            curto = item
        else:
            pass

    return lista_de_nomes[curto].capitalize()


def testa_menor_nome():
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
    lista2 = ['Ab',
              'maria',
              'Jequitinhonha',
              'pa ',
              ' Isabela ',
              'Joana',
              'Tamanduateí',
              'abacaxibacate',
              'Joao'
              ]

    if menor_nome(lista1)=='Paasasasasas':
        
        print( "Passou com 'paasasasasas'")
    else:
        
        print( 10*"#", "ERRO!!! Devolveu {} como mais curto!".format(menor_nome(lista1)), 10*"#")
    
    if menor_nome(lista2)=='Ab':
               
        print( "Passou com 'Ab'")
    else:
        print( 10*"#", "ERRO!!! Devolveu {} como mais curto!".format(menor_nome(lista2)), 10*"#")
    

