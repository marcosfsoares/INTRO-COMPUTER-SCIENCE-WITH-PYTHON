class Carro2:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano    = ano
        self.cor    = cor

meu_carro = Carro2("Ferrari", 1980, "Vermelho")

def main():
    carro1 = Carro("brasilia", 1968, "amarela", 80)
    carro2 = Carro("fuscão", 1981, "preto", 95)


    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)


class Carro:
    def __init__(self, modelo, ano, cor, vel_maxima):
        self.modelo = modelo
        self.ano    = ano
        self.cor    = cor
        self.vel    = 0
        self.maxV   = vel_maxima #velocidade maxima


    def imprima(self):
        if self.vel == 0: #parado para ver o ano
            print("%s %s %d"%(self.modelo, self.cor, self.ano)  )
        elif self.vel < self.maxV:
            print("%s %s indo a %d Km/h"%(self.modelo, self.cor, self.vel))
        else:
            print("%s %s indo muito raaaaaapiiiiiiidoooooooo!"%(self.modelo, self.cor))

    def acelere(self, veloc):
        self.vel = veloc
        if self.vel > self.maxV:
            self.vel = self.maxV
        self.imprima()

    def pare(self):
        self.vel = 0
        self.imprima()

        

main()



                                                
