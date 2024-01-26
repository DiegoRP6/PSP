import socket

def get_ip_address(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        print(f"The IP address of {domain_name} is {ip_address}")
    except socket.error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    domain_name = input("Enter the domain name: ")
    get_ip_address(domain_name)