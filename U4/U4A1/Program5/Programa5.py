import requests
import time

def verificar_sitio_web(url):
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print(f"¡El sitio web {url} está en línea!")
        else:
            print(f"¡El sitio web {url} está caído! Código de estado: {respuesta.status_code}")
    except requests.ConnectionError:
        print(f"No se pudo conectar a {url}")

def main():
    url = input("Por favor, introduce la URL del sitio web que deseas verificar: ")
    intervalo = 5  # Intervalo en segundos entre cada verificación

    while True:
        verificar_sitio_web(url)
        time.sleep(intervalo)

if __name__ == "__main__":
    main()
