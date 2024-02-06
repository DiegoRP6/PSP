import requests

def obtener_pais_por_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        pais = datos.get("country", "No disponible")
        return pais
    else:
        return "Error al obtener la información."

def main():
    ip = input("Ingrese la dirección IP: ")
    pais = obtener_pais_por_ip(ip)
    print(f"La dirección IP {ip} está registrada en el país: {pais}")

if __name__ == "__main__":
    main()
