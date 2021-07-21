def conta_letras(frase, contar="vogais"):
    frase = frase.lower().strip()
    vogais = ["a", "e", "i", "o", "u"]
    if contar == "vogais":
        return sum([frase.count(vogal) for vogal in vogais])
        #return frase.count("a")+frase.count("e")+frase.count("i")+frase.count("o")+frase.count("u")
    elif contar == "consoantes":
        for vogal in vogais:
            frase = frase.replace(vogal, "")
        return len([letra for letra in frase if "a"<=letra<="z"])
    else:
        pass
                
                
        
