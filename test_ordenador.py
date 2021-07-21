import Ordenador
import pytest

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return Ordenador.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c = Ordenador.ContaTempos()
        return c.lista_quase_ordenada(1000)

    @pytest.fixture
    def l_aleat(self):
        c = Ordenador.ContaTempos()
        return c.lista_aleatoria(1000)

    def esta_ordenada(self, lista):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i+1]:
                return False
        return True
    
    def test_bolha_curta_aleat(self, o, l_aleat):
        o.bolha_curta(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def test_selecao_direta_aleat(self, o, l_aleat):
        o.selecao_direta(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def test_bolha_curta_quase(self, o, l_quase):
        o.bolha_curta(l_quase)
        assert self.esta_ordenada(l_quase)

    def test_selecao_direta_quase(self, o, l_quase):
        o.selecao_direta(l_quase)
        assert self.esta_ordenada(l_quase)
