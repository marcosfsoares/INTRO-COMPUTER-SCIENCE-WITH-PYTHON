def n_primos(n):
    contprimo=0
    contatotal=n
    descobreprimo=2
    naoprimo=False
    while contatotal<=n and contatotal>1:
        while descobreprimo<contatotal and naoprimo==False:
            
            if contatotal%descobreprimo!=0:
                naoprimo=False
            elif contatotal==descobreprimo==2:
                naoprimo=False
            else:
                naoprimo=True
            descobreprimo=descobreprimo+1
        if naoprimo==False:    
            contprimo=contprimo+1
        contatotal=contatotal-1
        naoprimo=False
        descobreprimo=2
    return contprimo
