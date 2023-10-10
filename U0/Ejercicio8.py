#Ejercicio 8:  
#Implementa un programa Python con un método llamado sum(int [] tabla) que muestre por pantalla el resultado de sumar 
#todos los elementos de la tabla pasada como parámetro.

tabla = [1, 4, 6, 2, 5, 2, 1]
resultado = 0

def sum_tabla(tabla):
    suma = 0
    for i in tabla:
        suma += i
    return suma

resultado = sum_tabla(tabla)
print("La suma de los elementos de la tabla es:", resultado)