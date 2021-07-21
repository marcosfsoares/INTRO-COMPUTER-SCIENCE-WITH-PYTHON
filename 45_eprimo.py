
def eh_primo(n):
    
    i=n-1
    primo=True
    
    while (i<n and i>1):
        if(n%i!=0):
            primo=True
       
        else:
            primo=False
            return primo
        i=i-1
        
        
    return primo
'''
def fatoresprimos(numero):
    contador=numero
    fator=2
    multiplicidade=0
    
    while contador<=numero and numero>1:
        if !eh_primo(contador)
            while(numero%contador==0):
                
                fator=contador
                multiplicidade=multiplicidade+1
                numero=numero/contador
                contador=numero

            
            contador=contador-1
        else:
            fator=contador
            multiplicidade=multiplicidade+1
            numero=numero/contador
            contador=numero
    '''
limite=int(input("Limite Maximo: "))
n=2
lista=[]
while n<=limite:
    if eh_primo(n):
        print(n, end=",")
        lista.append(n)
    n=n+1
print("")
print(lista)
