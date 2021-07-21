
def é_hipotenusa(n):

    hipotenusa=False
    c1=c2=1
    while(c1<=n):
        while(c2<=n):
            if(n**2==(c1**2+c2**2)):
                hipotenusa=True
                return hipotenusa
            c2=c2+1
        c1=c1+1
        c2=1
    return hipotenusa

def soma_hipotenusas(n):
    soma=0
    i=n
    
    while(i>=1):
        
        if é_hipotenusa(i):
           soma=soma+i
        i=i-1
       
    return soma

    
                
        
