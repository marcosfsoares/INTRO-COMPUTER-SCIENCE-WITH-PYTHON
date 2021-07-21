def incomodam(n):
    if n <= 0 or int(n) != n:
        return ""

    return "incomodam " + incomodam(n-1)


def elefantes(n):
    frase1 = "Um elefante incomoda muita gente"
    frase2 = " elefantes incomodam muita gente"

    if n <= 0 or int(n) != n:
        return ""
    elif n == 1:
        return frase1
    elif n == 2:
        return elefantes(n-1) + "\n" + str(n) + " elefantes " + incomodam(n) + "muito mais"

    muita_gente = str(n-1) + frase2
    muito_mais = str(n) + " elefantes " + incomodam(n) + "muito mais"

    return elefantes(n-1) + "\n" + muita_gente + "\n" + muito_mais

print(elefantes(5))