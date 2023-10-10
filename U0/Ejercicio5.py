#Ejercicio 5:  
#Implementa un programa Python que solicite al usuario una cadena de caracteres (String) y muestre por pantalla el número 
#de veces que aparece la sub-cadena “aaa” dentro de dicho String.

cadena = input("Ingresa una cadena de caracteres que contenga aaa: ")
contador = 0
contador_aaa = 0

for i in cadena:
    if i == 'a' :
        contador_aaa += 1
    else:
        contador_aaa = 0
    if contador_aaa == 3:
        contador += 1
        contador_aaa = 1 #Para evitar sobreposiciones       
        
print("Número de veces que aparece la subcadena 'aaa':", contador)