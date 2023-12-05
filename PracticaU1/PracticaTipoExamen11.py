#Implementa en python un código de Productor Consumidor mediante cola sincronizada tal que:
#-El productor produce números enteros mayor que 10 y menor que 1000, el productor produce 10 números cada vez que los almacena en la cola y el tiempo de espera entre la generación de un número y otro es de PT segundos (1 punto)
#-El consumidor lee X números de la cola de golpe, calcula el MCD de esos X números .(1,5 punto)
#
#el tiempo de espera entre la lectura de X elementos cola y la siguiente lectura de los siguientes X elementos es de  CT segundos (1 punto)
#Prueba el algoritmo con los distintos casos usando una relación de productor:consumidor de     
#1:1   con PT=1  CT=4 y X=3 (0,5 puntos)
#4:2 con PT=2  CT=4 y X=2 (0,5 puntos)
#2:10 con PT=1  CT=10 y X=4 (0,5 puntos)

import threading
import queue
import random
import time
from math import gcd

class Productor(threading.Thread):
    def __init__(self, queue, PT):
        threading.Thread.__init__(self)
        self.queue = queue
        self.PT = PT
        
    def run(self):
        while True:
            for _ in range(10):
                self.queue.put(random.randint(10,1000))
                time.sleep(self.PT)

class Consumidor(threading.Thread):
    def __init__(self, queue, CT, X):
        threading.Thread.__init__(self)
        self.queue = queue
        self.CT = CT
        self.X = X
        
    def run(self):
        while True:
            numeros = []
            for i in range(self.X):
                numeros.append(self.queue.get())
                print("Consumiendo: " + str({numeros[i]}))
            
            mcd = numeros[0]
            for i in numeros[1:]:
                mcd = gcd(mcd, i)
            print(f"Consumidos: {numeros}, MCD: {mcd}")
            time.sleep(self.CT)


if __name__ == "__main__":
    queue = queue.Queue()

    def apartado1():
        # Relación 1:1 con PT=1, CT=4 y X=3
        PT_1_1 = 1
        CT_1_1 = 4
        X_1_1 = 3
        relacion_1_1 = 1
        hilos_productores_1_1 = [Productor(queue, PT_1_1) for _ in range(relacion_1_1)]
        hilos_consumidores_1_1 = [Consumidor(queue, CT_1_1, X_1_1) for _ in range(relacion_1_1)]

        for hilo in hilos_productores_1_1:
            hilo.start()
        for hilo in hilos_consumidores_1_1:
            hilo.start()

        for hilo in hilos_productores_1_1:
            hilo.join()
        for hilo in hilos_consumidores_1_1:
            hilo.join()

    def apartado2():
        # Relación 4:2 con PT=2, CT=4 y X=2
        PT_4_2 = 2
        CT_4_2 = 4
        X_4_2 = 2
        relacion_4_2 = 4
        hilos_productores_4_2 = [Productor(queue, PT_4_2) for _ in range(relacion_4_2)]
        hilos_consumidores_4_2 = [Consumidor(queue, CT_4_2, X_4_2) for _ in range(relacion_4_2)]

        for hilo in hilos_productores_4_2:
            hilo.start()
        for hilo in hilos_consumidores_4_2:
            hilo.start()

        for hilo in hilos_productores_4_2:
            hilo.join()
        for hilo in hilos_consumidores_4_2:
            hilo.join()

    def apartado3():
        # Relación 2:10 con PT=1, CT=10 y X=4
        PT_2_10 = 1
        CT_2_10 = 10
        X_2_10 = 4
        relacion_2_10 = 2
        hilos_productores_2_10 = [Productor(queue, PT_2_10) for _ in range(relacion_2_10)]
        hilos_consumidores_2_10 = [Consumidor(queue, CT_2_10, X_2_10) for _ in range(relacion_2_10)]

        for hilo in hilos_productores_2_10:
            hilo.start()
        for hilo in hilos_consumidores_2_10:
            hilo.start()

        for hilo in hilos_productores_2_10:
            hilo.join()
        for hilo in hilos_consumidores_2_10:
            hilo.join()

    #apartado1()
    #apartado2()
    apartado3()