import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Cargar la clave pública de B
with open('publicB.pem', 'rb') as f:
    public_key = RSA.import_key(f.read())

# Establecer conexión
host = '192.168.1.101'  # Dirección IP de B
port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Enviar la clave pública a B
client_socket.send(public_key.export_key())

# Leer el archivo que se va a enviar
file_to_send = 'archivo_a_enviar.txt'
with open(file_to_send, 'rb') as f:
    data = f.read()

# Encriptar el archivo con la clave pública de B
cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted_data = cipher_rsa.encrypt(data)

# Enviar el archivo encriptado
client_socket.send(encrypted_data)

# Cerrar la conexión
client_socket.close()