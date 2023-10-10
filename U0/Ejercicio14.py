# Ejercicio 14: Realiza un programa en Python en el que muestres un menú que te permita 3 opciones:
#                 - 1. Volcado (escritura) de una lista con todos los números pares comprendidos entre 0 y 100.
#                 - 2. Mostrar (lectura) por pantalla el contenido del fichero de texto creado.
#                 - 3. Salir del Programa.

def escribir_pares():
    with open('numeros_pares.txt', 'w') as archivo:
        for i in range(0, 101, 2):
            archivo.write(str(i) + '\n')

def mostrar_contenido():
    try:
        with open('numeros_pares.txt', 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print('El archivo no existe. Aún no se ha realizado el volcado.')

def menu():
    while True:
        print("MENU:")
        print("1. Volcado de números pares entre 0 y 100 en un archivo")
        print("2. Mostrar contenido del archivo")
        print("3. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            escribir_pares()
            print("Números pares entre 0 y 100 volcados en el archivo.")
        elif opcion == '2':
            mostrar_contenido()
        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()