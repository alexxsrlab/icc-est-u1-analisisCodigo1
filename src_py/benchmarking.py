from metodo_ordenamiento import MetodosOrdenamiento
import random
import time
class Benchmarking: 

    #Public Benchmarking
    def __init__(self):
        print('Benchmarking instanciado')
        self.mO = MetodosOrdenamiento()
        arreglo = self.build_arreglo(10000)  
    
    def build_arreglo(self, size):
        return [random.randint(0, 10000) for _ in range(size)]

    def medir_tiempo(self, funcion, arreglo):
        inicio = time.perf_counter()
        funcion(arreglo)
        fin = time.perf_counter()
        return (fin - inicio)

        """
        self.mO = MetodosOrdenamiento()

        arreglo = self.build_arreglo(10000)

        tarea = lambda:self.mO.sort_bubble(arreglo)

        ##milisegundos = self.contar_cont_current_time_milles(tarea)
        nanosegundos = self.contar_con_nano_time(tarea)

        ##print(f'Tiempo en milisegundos: {milisegundos}' )
        print(f'Tiempo en nanosegundos: {nanosegundos}' )

        area = lambda:self.mO.sort_burbuja_mejorado_optimizado(arreglo)
        nanosegundos = self.contar_con_nano_time(tarea)
        print(f'Tiempo en nanosegundos con burbuja mejorado: {nanosegundos}' )

        area = lambda:self.mO.sort_seleccion(arreglo)
        nanosegundos = self.contar_con_nano_time(tarea)
        print(f'Tiempo en nanosegundos con metodo seleccion: {nanosegundos}' )
        
        area = lambda:self.mO.sort_shell(arreglo)
        nanosegundos = self.contar_con_nano_time(tarea)
        print(f'Tiempo en nanosegundos con metodo shell: {nanosegundos}' )

    def build_arreglo(self, tamano):
        arreglo = []

        for i in range (tamano):
            numero = random.randint(0,99999)
            arreglo.append(numero)
        return arreglo
        

    def contar_cont_current_time_milles(self, tarea):

        inicio = time.time()
        tarea()
        fin = time.time()
        return (fin - inicio)
              

    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return ( fin - inicio) / 1_000_000_000.0
        """