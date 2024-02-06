import whois

def get_whois_info(ip_address):
    try:
        whois_info = whois.whois(ip_address)
        return whois_info
    except whois.parser.PywhoisError as e:
        return f"Error al buscar la información WHOIS: {str(e)}"

def main():
    ip_address = input("Ingrese la dirección IP o el nombre de host: ")
    result = get_whois_info(ip_address)
    
    print(f"La información WHOIS para {ip_address} es:\n{result}")

if __name__ == "__main__":
    main()
