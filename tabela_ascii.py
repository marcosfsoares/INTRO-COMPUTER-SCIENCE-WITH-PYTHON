print("Tabela ASCII de 32 a 127: ")
for i in range(32, 128, 3):
    print("ASCII[ %3d ] = '%s'  |  ASCII[ %3d ] = '%s'  |  ASCII[ %3d ] = '%s'"%
    (i, chr(i), i+1, chr(i+1), i+2, chr(i+2)))
