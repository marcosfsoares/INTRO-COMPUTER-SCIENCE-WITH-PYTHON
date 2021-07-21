def encontra_impares(lista):
    if len(lista) == 0:
        return lista

    impar = [lista[0]]
    if lista[0] % 2 == 0:
        return encontra_impares(lista[1:])
    else:
        impar.extend(encontra_impares(lista[1:]))
    return impar



