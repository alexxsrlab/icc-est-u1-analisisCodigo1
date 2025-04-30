import java.util.Random;
public class Brenchmarking {
    private MetodosOrdenamiento mOrdenamiento;
    public Brenchmarking(){
        long currentMillis = System.currentTimeMillis();
        long currentNano = System.nanoTime();

        System.out.println(currentMillis);
        System.out.println(currentNano);

        mOrdenamiento = new MetodosOrdenamiento();
        int[] arreglo = generarArreglosAleatorio(10000);
        
        Runnable tarea =()-> mOrdenamiento.burbujaTradicional(arreglo);

        double tiempoDuracionMillis =  medirConCurrentTimeMiles(tarea);
        double tiempoDuracionNano =  medirConNanoTime(tarea);

        System.out.println("Tiempo en milsegundos : " + tiempoDuracionMillis);
        System.out.println("Tiempo en nanosegundos: " + tiempoDuracionNano);

    }

    private int[] generarArreglosAleatorio(int tamano){
        
        int [] array = new int[tamano];
        Random random = new Random();
        for (int i=0; i < tamano; i++){
            array[i] = random.nextInt(100000);
        }
        return array;
    }

    public double medirConCurrentTimeMiles(Runnable tarea) {
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        double tiempoSegundos = (fin - inicio) / 1000.0;
        return tiempoSegundos;
    }

    public double medirConNanoTime(Runnable tarea) {
        long inicio = System.nanoTime();
        tarea.run();
        long fin =System.nanoTime();
        return (fin - inicio) / 1_000_000_000.0;
    }
}
