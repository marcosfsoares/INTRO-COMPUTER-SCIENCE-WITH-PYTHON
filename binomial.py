def fatorial(n):
    valor=1

    while(n>0):
         valor = valor*n
         n=n-1
    return valor

def binomial(n,k):
    return ((fatorial(n))/(fatorial(k)*fatorial(n-k)))

    
