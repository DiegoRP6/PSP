#Ejercicio 1: 
#utilizando el módulo de subprocesos múltiples, escriba un programa Python simple de la siguiente manera:
#● Cree un grupo de subprocesos para ejecutar tareas simultáneas.
#● El tamaño de la piscina debe ser 10.
#● El hilo debe recibir como entrada un número [id] (identificador único para cada uno de los
#hilos, comenzando desde 1) y un número [número_de_escrituras] (número de veces el
#hilo escribirá el mensaje).
#● Cada subproceso debe estar inactivo durante un período de tiempo aleatorio (entre 100 y 300
#milisegundos) y escribe el mensaje ("Soy 1", "Soy 2", etc.) un número aleatorio de veces
#entre 5 y 15.

import random
import threading
import time


def multithread(id, number_of_writings):
    for i in range(number_of_writings):

        delay = random.randint(100, 300) /1000
        print(f"Soy {id} escribiendo el mensaje {i+1} ")
        time.sleep(delay)


if __name__ == "__main__":
    pool_size = 10
    threads = []

    for thread in range(pool_size):
        number_of_writings = random.randint(1, 15)
        thread = threading.Thread(target=multithread, args=(thread + 1, number_of_writings))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    print("Todos los hilos han terminado")





