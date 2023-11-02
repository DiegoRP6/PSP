#Ejercicio 1: utilizando el módulo de multiprocesamiento, escriba un programa Python simple de la siguiente manera:
#
#Cree un grupo de trabajadores para ejecutar tareas paralelas.
#El tamaño del grupo debe ser la cantidad de núcleos de CPU disponibles en su nodo menos 1 (
#8 núcleos > grupo de 7 trabajadores).
#Escriba una función para que se ejecute en paralelo, llámela my_id. 
#La función debe recibir como entrada la identificación de la tarea. Cuando se llama, la función 
#imprimirá en la pantalla un mensaje con el formato: “Hola, soy ID de trabajador (con PID)”. 
#Donde ID debe reemplazarse con el número de tarea asignado al trabajador y PID con el ID de proceso 
#del trabajador corriendo.
#Ejecute tareas en paralelo usando la función de mapa, para un total de tareas igual al doble de la 
# cantidad de núcleos de CPU en su nodo.

import multiprocessing
import os

def my_id(task_id):
    worker_id = task_id
    process_id = os.getpid()
    print(f"Hola, soy el trabajador {worker_id} (con PID {process_id})")

if __name__ == '__main__':
    num_nucleos = multiprocessing.cpu_count()
    pool_size = num_nucleos - 1

    processes = []
    for task in range(pool_size * 2):
        process = multiprocessing.Process(target=my_id, args=(task,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()