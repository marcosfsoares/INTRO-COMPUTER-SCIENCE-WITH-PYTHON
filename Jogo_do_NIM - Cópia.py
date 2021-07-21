''' JOGO NO NIM
n é o número inicial de peças
m é o número máximo de peças que é possível retirar em uma rodada'''

def computador_escolhe_jogada(n,m):
    escolhida=m
    while(escolhida>0):
        if((n-escolhida)==0):
            return escolhida
        elif((n-escolhida)%(m+1)==0):
            return escolhida
        else:
            escolhida=escolhida-1
        
               
    return m

def usuario_escolhe_jogada(n,m):
    quantas_pecas_tirar=int(input("Quantas peças você vai tirar? "))
    if(quantas_pecas_tirar>m or quantas_pecas_tirar<1 or quantas_pecas_tirar>n):
        print("Oops! Jogada inválida! Tente de novo.")
        quantas_pecas_tirar=usuario_escolhe_jogada(n,m)
          
    return quantas_pecas_tirar
    
def partida():
    pecas=int(input("Quantas peças? "))
    pecas_por_jogada=int(input("Limite de peças por jogada? "))

    while(pecas<=pecas_por_jogada or pecas_por_jogada==0):
        
        pecas=int(input("Quantas peças? "))
        pecas_por_jogada=int(input("Limite de peças por jogada? "))
                
    if((pecas%(pecas_por_jogada+1))==0):
        print("Voce começa!")
        voce_comeca=True
        usuario=0
       
    else:
        print("Computador começa!")
        voce_comeca=False
        computador=0
          
    while(pecas>=1):
        if(voce_comeca==True):
            usuario = usuario_escolhe_jogada(pecas,pecas_por_jogada)
            if(usuario==1):
                print("Voce tirou uma peça.")
            else:
                print("Voce tirou",usuario,"peças.")
            voce_comeca=False
            pecas=pecas-usuario

        elif(voce_comeca==False):
            
            computador = computador_escolhe_jogada(pecas,pecas_por_jogada)
            if(computador==1):
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou",computador,"peças.")
            voce_comeca=True
            pecas=pecas-computador
            
        if(pecas==1):
            print("Agora resta apenas uma peça no tabuleiro.")
        elif(pecas>1):
            print("Agora restam", pecas ,"peças no tabuleiro.")
        elif(pecas==0):
            if (voce_comeca==True):
                print("Fim do jogo! O computador ganhou!")
                return False
            else:
                print("Fim do jogo! Voce ganhou!")
                return True
            
            
        else:
            print("ERRO FATAL - PEÇAS RESTANTES NÃO PODEM SER NEGATIVAS")
  
def campeonato():
    rodada=1
    voce=0
    computador=0
    while(rodada>=1 and rodada<=3):
        print("****Rodada",rodada,"****")
        if partida():
            voce=voce+1
        else:
            computador=computador+1
        rodada = rodada+1
    
    print("**** Final do campeonato! ****")
    print("Placar: Você", voce, "X", computador,"Computador")
    
def main():
    escolha=0
    while(escolha<1 or escolha>2):
        print("Bem-vindo ao jogo do NIM! Escolha:")
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato")
               
        escolha=int(input(""))
      
            
        if(escolha==1):
            print("Voce escolheu uma partida isolada")
            partida()
        elif(escolha==2):
            print("Voce escolheu um campeonato")
            campeonato()
        
    

main()
 
