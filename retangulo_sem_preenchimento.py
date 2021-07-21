
def main():
    largura=int(input("digite a largura:"))
    altura=int(input("digite a altura:"))
    var=largura
    var2=altura
    while altura>0:
        while largura>0:
            if altura==1 or altura==var2:
                print("#", end="")
            elif (altura>1 or altura<var2) and (largura==1 or largura==var):
                print("#", end="")
            else:
                print(" ", end=(""))
            largura=largura-1
        
        print(end='\n')       
        altura=altura-1
        largura=var

main()
