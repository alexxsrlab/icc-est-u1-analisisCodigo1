from benchmarking import Benchmarking
from metodo_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt
from datetime import datetime
if __name__ == "__main__":
    print("Funciona")
    
    bench = Benchmarking()
    metodos = MetodosOrdenamiento()

    tamanios = [500, 1000, 2000]
    resultados = []

    # Asociar cada método con su función correspondiente
    metodoss_dic = {
        "burbuja": metodos.sort_bubble,
        "burbuja mejorado": metodos.sort_burbuja_mejorado_optimizado,
        "seleccion": metodos.sort_seleccion,
        "shell": metodos.sort_shell
    }

    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)

        for nombre, funcion_metodo in metodoss_dic.items():
            # Copiar el arreglo para que cada método trabaje con el mismo input original
            arreglo_copia = arreglo_base.copy()
            tiempo_resultado = bench.medir_tiempo(funcion_metodo, arreglo_copia)
            resultados.append((tam, nombre, tiempo_resultado))
        
    for tam, nombre, tiempo in resultados:
        print(f'Tamaño: {tam} | Método: {nombre} | Tiempo: {tiempo:.6f} segundos')  
    
    # Preparar los datos para graficar
    tiempos_by_metodo = {nombre: [] for nombre in metodoss_dic}
    
    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)
    '''
    plt.figure(figsize=(10, 6))
    
    # Graficar los tiempos por método
    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label=nombre, marker = "o")  # Cada línea con su nombre
    
    
    plt.title("Comparación de Métodos de Ordenamiento")  
    plt.xlabel("Tamaño de los arreglos")
    plt.ylabel("Tiempo de ejecucion")
    plt.legend()  
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    plt.plot(x, y, label = "Linea", color = "blue")             

    ##Agregar parametros
    plt.title("Mi primer grafico")  
    plt.xlabel("Eje X")         
    plt.ylabel("Eje Y") 

    ##Agregar leyenda 
    plt.legend()    

    ##Cuadricula 
    plt.grid(True)

    ##Mostrar mi ventana            
    plt.show()      
'''
    ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    nombre_autor = "ARIEL BADILLO"

    # Crear una figura con 2 subgráficos (1 fila, 2 columnas)
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    fig.canvas.manager.set_window_title(f"{nombre_autor} - {ahora}")

    # Subgráfico 1: Comparación de tiempos
    for nombre, tiempos in tiempos_by_metodo.items():
        axs[0].plot(tamanios, tiempos, label=nombre, marker="o")

    axs[0].set_title("Comparación de Tiempos de Ejecución de Algoritmos de Ordenamiento")
    axs[0].set_xlabel("Tamaño del arreglo")
    axs[0].set_ylabel("Tiempo de ejecución (segundos)")
    axs[0].legend()
    axs[0].grid(True)

    # Subgráfico 2: Línea de ejemplo
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    axs[1].plot(x, y, label="Línea 1", color="blue")
    axs[1].set_title("Gráfico de Ejemplo con Matplotlib")
    axs[1].set_xlabel("Eje X")
    axs[1].set_ylabel("Eje Y")
    axs[1].legend()
    axs[1].grid(True)

    # Título global con nombre y fecha
    fig.suptitle(f"{nombre_autor} – {ahora}", fontsize=14, fontweight='bold')

    plt.tight_layout(rect=[0, 0, 1, 0.95])  # deja espacio para el título
    plt.show()
    