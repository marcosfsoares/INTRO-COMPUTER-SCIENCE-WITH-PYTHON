def maximo(x,y,z):
    if ((x>=y and x>z) or (x>y and x>=z)):
        return x
    elif ((y>=x and y>z) or (y>x and y>=z)):
        return y
    elif ((z>=x and z>y) or (z>z and z>=y)):
        return z
    else:
        return x
