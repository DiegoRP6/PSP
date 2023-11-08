#Ejercicio 2: utilizando el módulo de multihilo, escriba un programa en Python de la siguiente manera:
#● Cree un grupo de multihilos para ejecutar tareas simultáneas.
#● El tamaño de la piscina debe ser 3.
#● Cree y complete una matriz de 100 números enteros aleatorios.
#● Ejecute los 3 multihilos para analizar los datos vectoriales. Uno de ellos debe mostrar la media, otro
#el valor máximo y mínimo, y el último la desviación estándar. Tenga en cuenta que
#Aunque estos hilos comparten el vector, sólo lo hacen para la lectura. Ninguno de ellos
#debe modificar cualquier valor del vector.

import random
import threading

def min_value(matriz):
    resultado = min(matriz)
    print(f"El valor mínimo de la matriz es {resultado}")

def max_value(matriz):
    resultado = max(matriz)
    print(f"El valor máximo de la matriz es {resultado}")

def average_value(matriz):
    resultado = sum(matriz) / len(matriz)
    print(f"El valor promedio de la matriz es {resultado}")

if __name__ == "__main__":
    pool_size = 3
    threads = []
    size_matriz = 100
    matriz = []
    
    for i in range(size_matriz):
        matriz.append(random.randint(0, 1000))

    functions = [min_value, max_value, average_value]

    for i in range(pool_size):
        thread = threading.Thread(target=functions[i], args=(matriz,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
