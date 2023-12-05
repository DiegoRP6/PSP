#
#Enunciado del Ejercicio: Problema Productor-Consumidor con Múltiples Productores y Consumidores
#
#Diseña un sistema de productor-consumidor con las siguientes características:
#
#a. Cuatro productores generan números aleatorios enteros, cada número mayor que 200 y menor que 1000.
#
#b. Tres consumidores leen conjuntos de 6 números de la cola de golpe y calculan el producto de esos 6 números.
#
#c. El tiempo de espera entre la generación de un número y otro por parte de cada productor es de 2 segundos.
#
#d. El tiempo de espera entre la lectura de un conjunto de 6 elementos por parte de cada consumidor y la siguiente lectura de otro conjunto de 6 elementos es de 4 segundos.
#
#Diseña el programa para que la relación entre productores y consumidores sea 2:3.
#
#Implementa el código utilizando el módulo threading de Python.

import threading
import queue
import random
import time

class Productor(threading.Thread):
    def __init__(self, cola, PT):
        threading.Thread.__init__(self)
        self.cola = cola
        self.PT = PT
        
    def run(self):
        while True:
            for _ in range(15 // relacion_consumidores_productores):
                self.cola.put(random.randint(200, 999))
                time.sleep(2)
            
class Consumidor(threading.Thread):
    def __init__(self, cola, CT):
        threading.Thread.__init__(self)
        self.cola = cola
        self.CT = CT
        
    def run(self):
        while True:
            numeros = []
            for i in range(6):
                numeros.append(self.cola.get())
                print("Consumiendo: " + str({numeros[i]}))
            
            producto = 1
            for i in numeros:
                producto *= i
            print(f"Consumidos: {numeros}, Producto: {producto}")
            time.sleep(self.CT)

if __name__ == "__main__":
    mi_cola = queue.Queue()
    relacion_consumidores_productores = 2
    PT = 2
    CT = 4

    # Crear hilos para productores y consumidores
    hilos_productores = [Productor(mi_cola, PT) for _ in range(4)]
    hilos_consumidores = [Consumidor(mi_cola, CT) for _ in range(3)]

    # Iniciar hilos
    for hilo in hilos_productores + hilos_consumidores:
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos_productores:
        hilo.join()

    for hilo in hilos_consumidores:
        hilo.join()