#Ejercicio 9:  
#Implementa un programa Python con un método llamado indexContains(String[] tabla, String cadena) que devuelva el índice 
#de la tabla cuyo valor es igual al valor de “cadena”. En caso de no haber ningún valor igual, devuelve -1

tabla = ["aquarius", "vino", "agua", "cerveza", "cocacola"]
cadena = "agua"

def indexContains(tabla, cadena):
    for i in range(len(tabla)):
        if tabla[i] == cadena:
            return i
    return -1




indice = indexContains(tabla, cadena)

if indice != -1:
    print("El índice de ", cadena , " en la tabla es: " , indice)
else:
    print(cadena, " no se encuentra en la tabla.")






