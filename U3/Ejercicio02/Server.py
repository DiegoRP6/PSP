import socket

def contar_vocales(mensaje):
    cantidad_vocales = sum(1 for caracter in mensaje if caracter.lower() in 'aeiou')
    return str(cantidad_vocales)

def iniciar_servidor():
    with socket.socket() as socket_servidor:
        socket_servidor.bind(('localhost', 8888))
        socket_servidor.listen()
        print("El servidor está escuchando conexiones entrantes...")

        conexion, direccion_cliente = socket_servidor.accept()
        with conexion:
            print(f"Conexión desde {direccion_cliente}")
            datos_recibidos = conexion.recv(1024)
            respuesta = contar_vocales(datos_recibidos.decode())
            conexion.sendall(respuesta.encode())

if __name__ == "__main__":
    iniciar_servidor()