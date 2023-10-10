#Ejercicio 3:  
#¡IMPLEMENTA TU PRIMER JUEGO! Realiza un programa Python que adivine el número. El programa generará un número aleatorio
# entre 0 y 20 y luego irá pidiendo números al usuario indicando “mayor” o “menor” según sea mayor o menor con respecto al 
#número generado aleatoriamente. El proceso termina cuando el usuario acierta, y deberá mostrar un mensaje de felicitaciones 
#junto al número de intentos que ha necesitado el usuario.
import random

Tries = 0
RandomNumber = random.randint(0,20)
Acierto = False


while Acierto == False:
    NumberIntroduced = int(input("Adivina un numero del 0 al 20"))
    if NumberIntroduced > RandomNumber:
        print("¡Menos!")
        Tries += 1
    elif NumberIntroduced < RandomNumber:
        print("¡Más!")
        Tries += 1
    else:
        Acierto = True
        print("¡ACERTASTE!")
        print("Numero de intentos  ", Tries)