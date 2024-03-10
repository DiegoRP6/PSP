import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Cargar la clave privada de B
with open('privateB.pem', 'rb') as f:
    private_key = RSA.import_key(f.read())

# Configurar el servidor
host = '192.168.1.101'  # Dirección IP de B
port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print("Esperando conexión...")

# Aceptar la conexión del cliente
client_socket, addr = server_socket.accept()
print("Conexión establecida con", addr)

# Recibir la clave pública de B desde A
public_key_data = client_socket.recv(2048)
public_key = RSA.import_key(public_key_data)

# Recibir el archivo encriptado
encrypted_data = client_socket.recv(4096)

# Desencriptar el archivo con la clave privada de B
cipher_rsa = PKCS1_OAEP.new(private_key)
decrypted_data = cipher_rsa.decrypt(encrypted_data)

# Guardar el archivo desencriptado
file_to_receive = 'archivo_recibido.txt'
with open(file_to_receive, 'wb') as f:
    f.write(decrypted_data)

# Cerrar la conexión
client_socket.close()
server_socket.close()