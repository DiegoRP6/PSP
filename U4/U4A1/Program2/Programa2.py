import socket

def scan_ports(ip, port_range):
    open_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Configura un tiempo de espera de 1 segundo para la conexión

        try:
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
                print(f"[*] Puerto {port} abierto")
            else:
                print(f"[!] Puerto {port} cerrado")

        except socket.error as e:
            print(f"[!] Error al escanear puerto {port}: {e}")

        finally:
            sock.close()

    return open_ports

def main():
    target_ip = input("Ingrese la dirección IP a escanear: ")
    start_port = int(input("Ingrese el puerto de inicio del rango: "))
    end_port = int(input("Ingrese el puerto final del rango: "))

    port_range = (start_port, end_port)

    open_ports = scan_ports(target_ip, port_range)

    if open_ports:
        print(f"[*] Puertos abiertos encontrados: {open_ports}")
    else:
        print("[*] No se encontraron puertos abiertos en el rango especificado.")

if __name__ == "__main__":
    main()
