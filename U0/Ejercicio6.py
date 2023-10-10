#Ejercicio 6:  
#Implementa un programa Python que solicite al usuario una cadena de caracteres (String) y muestre por pantalla dicha cadena, 
#pero con el primer y último carácter cambiados de posición.

cadena = input("Escribe una cadena: ")

if len(cadena) >= 2:
    primer_caracter = cadena[0]
    ultimo_caracter = cadena[-1]
    

    cadena_intercambiada = ultimo_caracter + cadena[1:-1] + primer_caracter
    
    print("Cadena con el primer y último carácter intercambiados:", cadena_intercambiada)
else:
    print("La cadena debe tener al menos dos caracteres para hacer el intercambio.")
