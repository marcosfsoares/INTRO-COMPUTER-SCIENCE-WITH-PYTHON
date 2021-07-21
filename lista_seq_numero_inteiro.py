def main():
    numero=[]
    n=0
    while n>=0:
        num=int(input("Digite o numero: "))
        if num==0:
            aux=n
            n=-2
        else:
            numero.append(num)
        n=n+1
    while aux>0:
        print(numero[aux-1])
        aux=aux-1
main()
def sequencia_inversa():
    numero=[]
    n=0
    while n>=0:
        numero.append(int(input("Digite o numero: ")))
        if numero[n]==0:
            del numero[n]
            n=-2
        n=n+1
    for a in range(len(numero),0,-1):
        
        print (numero[a-1])
   
