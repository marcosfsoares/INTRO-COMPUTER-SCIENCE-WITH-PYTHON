
def maiusculas(frase):
    ''' Recebe uma frase como parâmetro e devolve uma string
    com letras maiúsculas que existem na frase, na ordem em
    que elas aparecem'''
    retorno = ""
    for caracter in frase:
        if ord("A")<= ord(caracter)<= ord("Z"):
            retorno += caracter

    return retorno    
