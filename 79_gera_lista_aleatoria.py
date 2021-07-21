def lista_grande(n: int):
    import random

    return [random.randint(0, n*10) for numero in range(n)]
