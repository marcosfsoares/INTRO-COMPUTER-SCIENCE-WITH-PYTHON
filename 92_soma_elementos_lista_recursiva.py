
if __name__ == '__main__':
    import pytest


def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    elif len(lista) == 0:
        return None
    soma = [lista[0]+lista[1]]

    return soma_lista(soma+lista[2:])

print(soma_lista([0,1,2]))


lista1 = [0, 1, 2, 3]
lista2 = []
lista3 = [2]
lista4 = [22, 33]
lista5 = [1, 2, 3]
lista6 = [10, 20, 30, 40, 50]

@pytest.mark.parametrize("lista, esperado", [
    (lista1, 6),
    (lista2, None),
    (lista3, 2),
    (lista4, 55),
    (lista5, 6),
    (lista6, 150),
    ])

def test_soma_param(lista, esperado):
    assert soma_lista(lista) == esperado

def test_soma_lista():
    lista1 = [0, 1, 2, 3]
    lista2 = []
    lista3 = [2]
    lista4 = [22, 33]
    lista5 = [1, 2, 3]
    lista6 = [10, 20, 30, 40, 50]

    assert soma_lista(lista1) == 6
    assert soma_lista(lista2) == None
    assert soma_lista(lista3) == 2
    assert soma_lista(lista4) == 55
    assert soma_lista(lista5) == 6
    assert soma_lista(lista6) == 150
    '''if soma_lista(lista1) == 6:
        print("Lista1 OK")
    else:
        print("Lista1: NOK")
    if soma_lista(lista2) == None:
        print("Lista2 OK")
    else:
        print("Lista2: NOK")
    if soma_lista(lista3) == 2:
        print("Lista3 OK")
    else:
        print("Lista3: NOK")
    if soma_lista(lista4) == 55:
        print("Lista4 OK")
    else:
        print("Lista4: NOK")

test_soma_lista()'''