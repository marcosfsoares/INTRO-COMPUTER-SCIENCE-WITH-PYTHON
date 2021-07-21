def fatorial(n):
    if n < 0:
        return 0
    valor=1

    while(n>0):
         valor = valor*n
         n=n-1
    return valor

import pytest

@pytest.mark.parametrize("entrada, valor_esperado", [
    (0, 1),
    (1, 1),
    (-10, 0),
    (4, 24),
    (5, 120)
    ])

def test_fatorial(entrada, valor_esperado):
    assert fatorial(entrada) == valor_esperado

'''
def test_fatorial():
    cont=1
    while (cont <=200):
        assert fatorial(cont)>0
        cont=cont+1 '''
        
