import multiprocessing

# Lista de números para calcular el promedio
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Valor compartido para almacenar la suma
suma_compartida = multiprocessing.Value('i', 0)

# Valor compartido para almacenar la cantidad de elementos
contador_compartido = multiprocessing.Value('i', 0)

# Función para calcular la suma y el contador de una porción de la lista
def calcular_parcial(inicio, fin, lista, suma_compartida, contador_compartido, lock):
    parcial_suma = sum(lista[inicio:fin])
    parcial_contador = len(lista[inicio:fin])

    # Actualizar los valores compartidos
    lock.acquire()
    suma_compartida.value += parcial_suma
    lock.release()

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    # Dividir la lista en secciones para cada proceso
    num_procesos = 4
    tamaño_seccion = len(numbers) // num_procesos
    procesos = []

    # Crear procesos para calcular la suma y el contador de las secciones de la lista
    for i in range(num_procesos):
        inicio = i * tamaño_seccion
        fin = (i + 1) * tamaño_seccion if i < num_procesos - 1 else len(numbers)
        proceso = multiprocessing.Process(target=calcular_parcial, args=(inicio, fin, numbers, suma_compartida, contador_compartido, lock))
        procesos.append(proceso)
        proceso.start()

    # Esperar a que todos los procesos terminen
    for proceso in procesos:
        proceso.join()

    # Calcular el promedio total
    promedio_total = suma_compartida.value / contador_compartido.value if contador_compartido.value != 0 else 0

    # Imprimir el resultado
    print("Promedio total:", promedio_total)