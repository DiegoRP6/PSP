import socket
import threading

def handle_client(client_socket, clients, scores, rounds_to_win, player_names):
    player_name = player_names[client_socket]

    print(f"[*] {player_name} se ha unido al juego.")

    while True:
        if scores[client_socket] >= rounds_to_win:
            print(f"[*] {player_name} ha ganado el juego.")
            break

        for current_round in range(rounds_to_win):
            try:
                client_socket.send(f"[*] Ronda {current_round + 1}. {player_name}, introduce cuántas monedas tienes en la mano: ".encode('utf-8'))
                num_coins = int(client_socket.recv(1024).decode('utf-8'))

                if num_coins < 0 or num_coins > 3:
                    raise ValueError(f"Número de monedas fuera del rango permitido para {player_name}: {num_coins}")

                total_coins = sum(clients.values())
                client_socket.send(f"[*] Adivina cuántas monedas en total: ".encode('utf-8'))
                guess = int(client_socket.recv(1024).decode('utf-8'))

                if guess != total_coins:
                    raise ValueError(f"La adivinanza no es igual al total de monedas entre los jugadores para {player_name}: {guess}")

                scores[client_socket] += 1
                client_socket.send(f"[*] ¡Correcto! Has ganado la ronda.\n".encode('utf-8'))
                print(f"[*] Puntuaciones actuales: {player_names[client_socket]}: {scores[client_socket]}")

            except (ValueError, IndexError):
                print(f"[*] Error en la entrada de {player_name}. Ignorando la ronda.")
                break

        if scores[client_socket] >= rounds_to_win:
            client_socket.send(f"¡Felicidades! Has ganado el juego con {scores[client_socket]} puntos.\n".encode('utf-8'))
            break

    client_socket.close()
    del clients[client_socket]
    print(f"[*] {player_name} se ha desconectado.")

def main():
    host = '127.0.0.1'
    port = 5555
    rounds_to_win = 3

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"[*] Servidor escuchando en {host}:{port}")

    clients = {}
    scores = {}
    player_names = {}

    while True:
        client, addr = server.accept()
        print(f"[*] Conexión aceptada desde {addr[0]}:{addr[1]}")

        player_name = f"Jugador {len(clients) + 1}"
        player_names[client] = player_name

        clients[client] = 3  # Inicia con 3 monedas por jugador
        scores[client] = 0

        client_handler = threading.Thread(target=handle_client, args=(client, clients, scores, rounds_to_win, player_names))
        client_handler.start()

if __name__ == "__main__":
    main()
