# raízes da equação desegundo grau ax2 + bx + c

def main():
    
    import math

    a = float(input("Digite o valor a para ax2:"))
    b = float(input("Digite o valor b para bx:"))
    c = float(input("Digite o valor c para c:"))

    delta = (b**2) - 4*a*c
    if delta < 0:
        print("Esta equação não possui raízes reais")
    else:
        x1 = ((-b) + math.sqrt(delta))/(2*a)
        x2 = ((-b) - math.sqrt(delta))/(2*a)
        if delta == 0:
            print("A raiz desta equação é", x1)
        else:
            if x1 < x2:
                print("As raízes da equação são", x1, "e", x2)
            else:
                print("As raízes da equação são", x2, "e", x1)


main()
