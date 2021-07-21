def maior_primo(x):
    cont=x-1
    primoencontrado=0
    if(x==2):
        primoencontrado=2
    else:
        while(x>2):
            while(primoencontrado==0):
            
                if (x%cont!=0):
                    if cont==2:
                        primoencontrado=x
                        x=1
                    else:
                        cont=cont-1
                else:
                    x=x-1
                    cont=x-1
    return primoencontrado
                    
                
