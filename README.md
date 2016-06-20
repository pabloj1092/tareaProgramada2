# tareaProgramada2

## Protocolo MESI
Para ejecutar el protocolo MESI basta con ejecutar el archivo main.py de la forma ./main.py
Luego se puede observar en los archivos log_p1 y log_p2 el estado en memoria de los datos tras ejecutadas las últimas diez instrucciones por cada procesador.
## Números Primos 
./primeNumbers
Para ejecutar el argoritmo de Criba se requiere tener instalada la librería Open MPI.
Luego de eso dentro del folder primeNumbers se ejecuta "make -f makefile"
Finalmente se ejecuta el programa "mpirun -np X run" donde X es el número de procesos deseados
