#Implementa en Python un código de Productor-Consumidor mediante una cola sincronizada que cumpla con las siguientes
# especificaciones:
#Productor
#Genera números enteros aleatorios, siendo cada número mayor que 50 y menor que 2000.
#Produce 15 números en cada iteración, almacenándolos en la cola.
#El tiempo de espera entre la generación de un número y otro es de PT segundos.
#Consumidor
#Lee X números de la cola de golpe.
#Calcula la suma de los cuadrados de esos X números.
#El tiempo de espera entre la lectura de X elementos de la cola y la siguiente lectura de los siguientes X elementos
# es de CT segundos.
#Parametros
#Relación Productor:Consumidor para cada caso.
#PT (tiempo de espera del productor entre generaciones de números).
#CT (tiempo de espera del consumidor entre lecturas de elementos).
#X (cantidad de elementos leídos por el consumidor en cada iteración).

#a. Relación 1:1 con PT=2, CT=6 y X=4.
#b. Relación 5:2 con PT=1, CT=3 y X=5.
#c. Relación 3:10 con PT=3, CT=8 y X=2.

import threading
import queue
import random
import time




class Productor(threading.Thread):
    def __init__(self, queue, PT):
        threading.Thread.__init__(self)
        self.queue = queue
        self.PT = PT
        
    def run(self):
        while True:
            for _ in range(15):
                self.queue.put(random.randint(50,2000))
                time.sleep(self.PT)
        
    
class Consumidor(threading.Thread):
    def __init__(self, queue,X,CT):
        threading.Thread.__init__(self)
        self.queue = queue
        self.X = X
        self.CT = CT
        
    def run(self):
        while True:
            numeros = []
            for i in range(self.X):
                numeros.append(self.queue.get())
                print("Consumiendo: " + str({numeros[i]}))
            
            suma_cuadrados = sum(x**2 for x in numeros)
            print(f"Consumidos: {numeros}, Suma de cuadrados: {suma_cuadrados}")
            time.sleep(self.CT)
            
#a. Relación 1:1 con PT=2, CT=6 y X=4.
q_1_1 = queue.Queue()       
p_1_1 = Productor(q_1_1, PT=2)
c_1_1 = Consumidor(q_1_1, X=4, CT=6)

#b. Relación 5:2 con PT=1, CT=3 y X=5.
q_5_2 = queue.Queue()       
p_5_2 = Productor(q_5_2, PT=1)
c_5_2 = Consumidor(q_5_2, X=5, CT=3)

#c. Relación 3:10 con PT=3, CT=8 y X=2.

q_3_10 = queue.Queue()       
p_3_10 = Productor(q_3_10, PT=3)
c_3_10 = Consumidor(q_3_10, X=2, CT=8)


#inicio de hilos

p_1_1.start()
c_1_1.start()

p_5_2.start()
c_5_2.start()

p_3_10.start()
c_3_10.start()

#continuacion y finalizacion de hilos

p_1_1.join()
c_1_1.join()

p_5_2.join()
c_5_2.join()

p_3_10.join()
c_3_10.join()