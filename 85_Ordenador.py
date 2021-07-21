import time
import random

class Ordenador:
    def selecao_direta(self, lista):
        fim = len(lista)

        for i in range(fim -1):
            # Inicialmente, o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
            lista[posicao_do_minimo], lista[i] = lista[i], lista[posicao_do_minimo]

    def bolha(self, lista):
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

    def bolha_curta(self, lista):
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if not trocou:
                return

    def insercao_direta(self, lista):
        fim = len(lista)
        

        for i in range(1, fim):
            j=i
            elemento = lista[i]
            print('elemento:', elemento)
                      
            while (j > 0 and lista[j-1] >elemento):
                print('elemento:', elemento)
                lista[j] = lista[j-1]
                print('Lista[j] = ', lista[j])
                print('O Valor de J: ', j, 'I igual a:',i)
                j -= 1

            lista[j]= elemento
            print('Lista[',j,'] igual a ', elemento)
            
    def insertionSort(self, arr):
      
        # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):
      
            key = arr[i]
      
            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            while j >=0 and key < arr[j] :
                    arr[j+1] = arr[j]
                    print('Lista[j] = ', arr[j+1])
                    print('O Valor de J: ', j+1, 'I igual a:',i)
                    j -= 1
            arr[j+1] = key        
            print('Lista[',j+1,'] igual a ', key)                                          
                                                
            
                
                
   


class ContaTempos:
    
    
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista
    
    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
        lista3 = lista1[:]

        o = Ordenador()

        print('*****Comparando com listas aleatórias*****')

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print('Bolha demorou {} segundos'.format(depois - antes))
        
        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print('Seleção Direta demorou {} segundos'.format(depois - antes))

        antes = time.time()
        o.bolha_curta(lista3)
        depois = time.time()
        print('Bolha Curta demorou {} segundos'.format(depois - antes))

        print('\n\n\n*****Comparando com listas quase ordenadas*****')

        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]
        lista3 = lista1[:]
        
        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print('Bolha demorou {} segundos'.format(depois - antes))
        
        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print('Seleção Direta demorou {} segundos'.format(depois - antes))

        antes = time.time()
        o.bolha_curta(lista3)
        depois = time.time()
        print('Bolha Curta demorou {} segundos'.format(depois - antes))
                    

                    
