import pytest


def fatorial(n):
    if n < 1:
        return 1
    else:
        return n * fatorial(n-1)


@pytest.mark.parametrize("entrada, esperado", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
    ])
def testa_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado
