def troca(x, y):
    aux = x
    x = y
    y = aux
    return x,y

x = 10
y = 20
troca (x,y)
print("x =", x,"e y =",y)
