#Ejercicio 2:  
#Escribe un programa Python que pregunte al usuario por 10 números enteros y muestre por pantalla el número total de veces 
#que el usuario ha introducido el 0, el número total de enteros mayores que 0 introducidos y el número total de 
#enteros menores que 0 introducidos.

Zero = 0
MoreZero = 0
LessZero = 0

for i in range(10):
    numero = int(input("Introduce un numero entero"))
    if numero == 0:
        Zero += 1
    elif numero > 0:
        MoreZero += 1
    else:
        LessZero += 1

print("Número de veces que se introdujo 0:", Zero)
print("Número de enteros mayores que 0:", MoreZero)
print("Número de enteros menores que 0:", LessZero)
