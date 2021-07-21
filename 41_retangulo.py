
def main():
    largura=int(input("digite a largura:"))
    altura=int(input("digite a altura:"))
    var=largura
    while altura>0:
        while largura>0:
            print("#", end="")
            largura=largura-1
            
        
        print(end='\n')
        altura=altura-1
        largura=var

main()

