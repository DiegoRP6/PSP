#Enunciado del Ejercicio: Problema Productor-Consumidor con Múltiples Productores y Consumidores
#
#Diseña un sistema de productor-consumidor con las siguientes características:
#
#a. Tres productores generan números aleatorios enteros, cada número mayor que 100 y menor que 500.
#
#b. Dos consumidores leen conjuntos de 8 números de la cola de golpe y calculan la suma de los cuadrados de esos 8 números.
#
#c. El tiempo de espera entre la generación de un número y otro por parte de cada productor es de 1 segundo.
#
#d. El tiempo de espera entre la lectura de un conjunto de 8 elementos por parte de cada consumidor y la siguiente lectura de otro conjunto de 8 elementos es de 3 segundos.
#Diseña el programa para que la relación entre productores y consumidores sea 2:1.
#Multithreading

import threading
import queue
import random
import time

queue = queue.Queue()

class Productor(threading.Thread):
    def __init__(self, queue, PT):
        threading.Thread.__init__(self)
        self.queue = queue
        self.PT = PT
        
    def run(self):
        while True:
            for _ in range(15 // relacion_productores_consumidores):
                queue.put(random.randint(100,500))
                time.sleep(1)

class Consumidor(threading.Thread):
    def __init__(self, queue, CT):
        threading.Thread.__init__(self)
        self.queue = queue
        self.CT = CT
        
    def run(self):
        while True:
            numeros = []
            for i in range(8):
                numeros.append(self.queue.get())
                print("Consumiendo: " + str({numeros[i]}))
            
            suma_cuadrados = sum(x**2 for x in numeros)
            print(f"Consumidos: {numeros}, Suma de cuadrados: {suma_cuadrados}")
            time.sleep(self.CT)


if __name__ == "__main__":
    relacion_productores_consumidores = 2
    PT = 1
    CT = 3

# Crear hilos para productores y consumidores
hilos_productores = []
hilos_consumidores = []
for _ in range(3):
    hilo = Productor(queue, PT)
    hilos_productores.append(hilo)
    hilo.start()

for _ in range(2):
    hilo = Consumidor(queue, CT)
    hilos_consumidores.append(hilo)
    hilo.start()


# Esperar a que todos los hilos terminen
for hilo in hilos_productores:
    hilo.join()

for hilo in hilos_consumidores:
    hilo.join()

