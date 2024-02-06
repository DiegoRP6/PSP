import socket

def main():
    host = '127.0.0.1'
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        try:
            num_coins = int(input("¿Cuántas monedas quieres guardar en tu mano? (0-3): "))
            if num_coins < 0 or num_coins > 3:
                raise ValueError("Por favor, elige un número válido de monedas (0-3).")

            client.send(f"{num_coins}\n".encode('utf-8'))

            guess = int(input("Adivina cuántas monedas en total: "))
            if guess < 0:
                raise ValueError("Números negativos no permitidos.")

            client.send(f"{guess}\n".encode('utf-8'))

            response = client.recv(1024).decode('utf-8')
            print(response)

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
