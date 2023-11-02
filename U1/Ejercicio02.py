#Ejercicio 2: utilizando el módulo de multiprocesamiento, escriba un programa Python simple de la siguiente manera:
#
#Cree un grupo de trabajadores para ejecutar tareas paralelas.
#El tamaño de la piscina debe ser 2.
#Escriba una función para que se ejecute en paralelo, llámela print_cube. 
#La función debe recibir como entrada un número [num]. Cuando se llama, la función imprimirá en la 
#pantalla un mensaje con el formato: “El cubo del número [num] es [cubo]”. Donde [cubo] debe 
#reemplazarse con el cubo del número recibido como entrada.
#Escriba una función para que se ejecute en paralelo, llámela print_square. 
#La función debe recibir como entrada un número [num]. Cuando se llama, la función imprimirá en 
#la pantalla un mensaje con el formato: “El cuadrado del número [num] es [cuadrado]”. 
#Donde [cuadrado] debe reemplazarse con el cuadrado del número recibido como entrada.
import multiprocessing

def print_cube(num):
    cube = num **3
    print(f"The cube of {num} + is {cube}")

def print_square(num):
    square = num**2
    print(f"The square of {num} is {square}")

if __name__ == '__main__':
    pool_size = 2
    numbers = range(10)

    cube_processes = []
    square_processes = []

    for num in numbers:
        cube_process = multiprocessing.Process(target=print_cube, args=(num,))
        square_process = multiprocessing.Process(target=print_square, args=(num,))

        cube_processes.append(cube_process)
        square_processes.append(square_process)

    for cube_process in cube_processes:
        cube_process.start()

    for square_process in square_processes:
        square_process.start()

    for cube_process in cube_processes:
        cube_process.join()

    for square_process in square_processes:
        square_process.join()
    

