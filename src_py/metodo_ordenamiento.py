class MetodosOrdenamiento:

    def sort_bubble(self , array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range (n):
            for j in range (i + 1 , n):
               if arreglo [i] > arreglo [j]:
                   arreglo [i] , arreglo [j] = arreglo[j] , arreglo [i]
        return arreglo


    def sort_burbuja_mejorado_optimizado(self , array):  
        arreglo = array.copy()
        n = len(arreglo)
        for i in range (n):
           for j in range (i+ 1 , n-1-i):
               if arreglo [j] > arreglo [j+1]:       
                   arreglo [j] , arreglo [j+1] = arreglo[j+1] , arreglo [j] 
        return arreglo


    def sort_seleccion (self, array):
        arreglo = array.copy()
        n = len(arreglo)    
        for i in range (n):
            iM = i
            for j in range (i+1, n):
                if arreglo [iM] > arreglo [j]:
                    iM = j

        return arreglo
    
    def sort_shell(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        gap = n // 2  # Comenzar con la mitad del tamaño del arreglo

        while gap > 0:
            for i in range(gap, n):
                temp = arreglo[i]
                j = i
                # Ordenar los elementos separados por gap
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap
                    arreglo[j] = temp
            gap //= 2  # Reducir el gap en cada iteración






















        return arreglo