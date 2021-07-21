import baskara_testavel
import pytest

@pytest.mark.parametrize("entrada,valor_esperado", [
    ((1,0,0),(1,0)),
    ((1,-5,6),(2,3,2)),
    ((10,10,10),0),
    ((10,20,10),(1,-1))
    ])

class TestBhaskara:
    @pytest.fixture
    def b(self):
        return baskara_testavel.Bhaskara()

    def test_bhaskara(self, b, entrada, valor_esperado):
        a,b,c = entrada
        assert b.calcula_raizes(a,b,c) == (valor_esperado)
'''

class TestBhaskara:

    @pytest.fixture
    def b(self):
        return baskara_testavel.Bhaskara()
    
    def testa_uma_raiz(self,b):
        assert b.calcula_raizes(1,0,0) == (1, 0)

    def testa_duas_raiz(self,b):
        assert b.calcula_raizes(1,-5,6) == (2, 3, 2)
        
    def testa_zero_raiz(self,b):
        assert b.calcula_raizes(10,10,10) == 0

    def testa_raiz_negativa(self,b):
        assert b.calcula_raizes(10,20,10) == (1, -1)



import baskara_testavel

class TestBhaskara:

    
    def testa_uma_raiz(self):
        b=baskara_testavel.Bhaskara()
        assert b.calcula_raizes(1,0,0) == (1, 0)

    def testa_duas_raiz(self):
        b=baskara_testavel.Bhaskara()
        assert b.calcula_raizes(1,-5,6) == (2, 3, 2)
        
    def testa_zero_raiz(self):
        b=baskara_testavel.Bhaskara()
        assert b.calcula_raizes(10,10,10) == 0
    def testa_raiz_negativa(self):
        b=baskara_testavel.Bhaskara()
        assert b.calcula_raizes(10,20,10) == (1, -1)'''
