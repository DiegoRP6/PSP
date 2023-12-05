#Diseña un sistema de productor-consumidor en Python utilizando una cola sincronizada. El productor generará cadenas de texto representando tareas, donde cada tarea es una acción a realizar. Sacará 10 tareas del sistema, almacenándolas en la cola.
#
#El consumidor leerá 2 tareas de la cola en cada iteración y calculará la longitud total de las dos cadenas de texto. El tiempo de espera entre la lectura de un conjunto de 2 tareas del la cola y la siguiente lectura será de 3 segundos.
#
#Establece una relación de 3:1 entre el productor y el consumidor. Es decir, por cada tres iteraciones del productor, el consumidor realizará una iteración.
#
#Ajusta el tiempo de espera entre generaciones de tareas (PT), el tiempo de espera del consumidor (CT), y la cantidad de elementos leídos por el consumidor en cada iteración (X) según consideres apropiado.

import threading
import queue
import random
import time
import psutil

q = queue.Queue()
PT = 2
CT = 3
X = 5

class Productor(threading.Thread):
    def __init__(self, queue, PT):
        threading.Thread.__init__(self)
        self.queue = queue
        self.PT = PT
        
    #Metodo run que almacene 3 tareas del psutil en la cola
    def run(self):
        while True:
            for _ in range(3):
                self.queue.put(psutil.cpu_times(random.randint(50,2000)))
                time.sleep(self.PT)
            print("Contenido de la cola: "+str(list(self.queue.queue)))

Productor(q, PT).start()
Productor(q, PT).join()
