import socket

def obtener_cantidad_vocales(mensaje):
    with socket.socket() as socket_cliente:
        socket_cliente.connect(('localhost', 8888))
        socket_cliente.sendall(mensaje.encode())
        respuesta = socket_cliente.recv(1024)
        print(f"Número de vocales en el mensaje: {respuesta.decode()}")

if __name__ == "__main__":
    mensaje_usuario = input("Ingresa un mensaje: ")
    obtener_cantidad_vocales(mensaje_usuario)