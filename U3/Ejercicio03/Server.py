import socket

def sumar_numeros(client_socket):
    suma = 0
    while True:
        numero = int(client_socket.recv(1024).decode('utf-8'))
        if numero == 0:
            break
        suma += numero
    return suma

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('127.0.0.1', 12345))
    servidor.listen(1)

    print("Servidor esperando conexión...")

    conexion, direccion = servidor.accept()
    print(f"Conexión establecida desde {direccion}")

    suma = sumar_numeros(conexion)
    print(f"La suma es: {suma}")

    conexion.close()
    servidor.close()

if __name__ == "__main__":
    main()
