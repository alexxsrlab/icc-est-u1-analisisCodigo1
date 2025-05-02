##import benchmarking as bm
from benchmarking import Benchmarking
from metodo_ordenamiento import MetodosOrdenamiento
if __name__ == "__main__":
    print("Funciona")
    
    bench = Benchmarking()
    metodos = MetodosOrdenamiento()

    tam = 10000
    arreglo_base = bench.build_arreglo(tam)

    metodoss_dic = {
        "burbuja": metodos.sort_bubble,
        "burbuja mejorado": metodos.sort_burbuja_mejorado_optimizado,
        "seleccion": metodos.sort_seleccion,
        "shell": metodos.sort_shell
    }

    tamanios = [5000, 10000, 10500]
    resultados = []

    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)

        for nombre, funcion_metodo in metodoss_dic.items():
            tiempo_resultado =bench.medir_tiempo(funcion_metodo, arreglo_base)
            resultados.append((tam, nombre, tiempo_resultado)) ## el tupla es un conjunto de datos que no se modifica
        
    for tam, nombre, tiempo in resultados:
        print(f'Tamaño:  {tam} Nombre:  {nombre} Tiempo:  {tiempo}')  