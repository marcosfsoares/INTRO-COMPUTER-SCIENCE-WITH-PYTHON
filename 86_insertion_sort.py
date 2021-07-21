def insertion_sort(lista):
        fim = len(lista)
        for i in range(1, fim):
      
            guarda_i = lista[i]
                 
            j = i
            while j >0 and guarda_i < lista[j-1]:
                    lista[j] = lista[j-1]
                    
                    j -= 1
            lista[j] = guarda_i        
        return lista
