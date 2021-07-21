# ax2 + bx + c

def main():
    
    import math

    a=float(input("Digite o valor a para ax2:"))
    b=float(input("Digite o valor b para bx:"))
    c=float(input("Digite o valor c para c:"))

    delta = (b**2) - 4*a*c
    if (delta < 0 ):
        print("esta equação não possui raízes reais")
    else:
        x1 = ((-b) + math.sqrt(delta))/(2*a)
        x2 = ((-b) - math.sqrt(delta))/(2*a)
        if (delta==0):
            print("a raiz desta equação é",x1)
        else:
            if (x1 < x2):
                print("as raízes da equação são",x1, "e",x2)
            else:
                print("as raízes da equação são",x2, "e",x1)
main()

def calculax1(a,b,c):
    import math
    delta = (b**2) - 4*a*c
    x1 = ((-b) + math.sqrt(delta))/(2*a)
    return x1

def calculax2(a,b,c):
    import math
    delta = (b**2) - 4*a*c
    x2 = ((-b) - math.sqrt(delta))/(2*a)
    return x2

def delta(a,b,c):
    delta = (b**2) - 4*a*c
    return delta

def baskara(a,b,c):
    if (delta(a,b,c) < 0 ):
        print("esta equação não possui raízes reais")
    else:
        x1 = calculax1(a,b,c)
        x2 = calculax2(a,b,c)
        if (delta(a,b,c)==0):
            print("a raiz desta equação é",x1)
        else:
            if (x1 < x2):
                print("as raízes da equação são",x1, "e",x2)
            else:
                print("as raízes da equação são",x2, "e",x1)


a=float(input("Digite o valor a para ax2:"))
b=float(input("Digite o valor b para bx:"))
c=float(input("Digite o valor c para c:"))

baskara(a,b,c)
    
