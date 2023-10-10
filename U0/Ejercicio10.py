#Ejercicio 10:  
#Implementa un método Python llamado mayorYmenor, el cual recibe como parámetro una tabla de Strings y muestra por pantalla
#el String con mayor longitud y el String con menor longitud.

strings = ["Ratón", "Agua", "Cocacola", "Llaves", "Ventilador", "Tarjeta"]

def mayorYmenor(strings):
    mayor = strings[0]
    menor = strings[0]
    for i in strings:
        if len(i) > len(mayor):
            mayor = i
        elif len(i) < len(menor):
            menor = i
    print("Mayor: ", mayor)
    print("Menor: ", menor)

mayorYmenor(strings)