# ax2 + bx + c
'''
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
'''
class Bhaskara:
    def delta(self,a,b,c):
        
        return (b**2) - 4*a*c

    def calcula_raizes(self,a,b,c):
        import math
        delt = self.delta(a,b,c)
        if delt== 0:
            x1 = ((-b)/(2*a))
            return 1, x1
        elif delt > 0:     
            x1 = ((-b) + math.sqrt(delt))/(2*a)
            x2 = ((-b) - math.sqrt(delt))/(2*a)
            return 2, x1, x2
        else:
            return 0
          



    def main(self):
        a=float(input("Digite o valor a para ax2:"))
        b=float(input("Digite o valor b para bx:"))
        c=float(input("Digite o valor c para c:"))
        print(self.calcula_raizes(a,b,c))
        
    

    
