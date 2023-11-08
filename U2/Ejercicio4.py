#Exercise 4: 
#Cree un programa que ejecute 10 hilos, 
# cada uno de los cuales sumará 100 números aleatorios entre el 1 y el 1000. 
#Muestre el resultado de cada hilo. 
#Ganará el hilo que consiga el número mas alto

import random
import threading

resultados = []

def sumar_numeros_aleatorios():
    total = sum(random.randint(1, 1000) for _ in range(100))
    resultados.append(total)

if __name__ == "__main__":
    pool_size = 10
    threads = []
    for thread in range(pool_size):
        thread = threading.Thread(target=sumar_numeros_aleatorios)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    for i, total in enumerate(resultados):
        print(f"Hilo {i}: {total}")

hilo_ganador = resultados.index(max(resultados))
print(f"El hilo ganador es {hilo_ganador} con un total de {resultados[hilo_ganador]}")