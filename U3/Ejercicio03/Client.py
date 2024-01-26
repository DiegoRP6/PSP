import socket

def enviar_numeros():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('127.0.0.1', 12345))

    while True:
        numero = int(input("Ingresa un número (o 0 para terminar): "))
        cliente.send(str(numero).encode('utf-8'))
        if numero == 0:
            break

    cliente.close()

if __name__ == "__main__":
    enviar_numeros()