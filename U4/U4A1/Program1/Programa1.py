from ftplib import FTP
from tkinter import Tk, filedialog

def descargar_archivo(ftp, nombre_archivo, ruta_local):
    with open(ruta_local, 'wb') as archivo_local:
        ftp.retrbinary('RETR ' + nombre_archivo, archivo_local.write)

def cargar_archivo(ftp, nombre_archivo, ruta_local):
    with open(ruta_local, 'rb') as archivo_local:
        ftp.storbinary('STOR ' + nombre_archivo, archivo_local)

def seleccionar_archivo(ftp):
    archivos = ftp.nlst()
    print("Archivos disponibles en el servidor FTP:")
    for i, archivo in enumerate(archivos, start=1):
        print(f"{i}. {archivo}")
    indice_archivo = int(input("Por favor, seleccione el número del archivo que desea descargar: ")) - 1
    return archivos[indice_archivo]

def seleccionar_archivo_local():
    root = Tk()
    root.withdraw()
    archivo = filedialog.askopenfilename()
    return archivo

def main():
    servidor_ftp = input("Introduce la dirección del servidor FTP: ")
    usuario = input("Introduce el nombre de usuario: ")
    contraseña = input("Introduce la contraseña: ")

    with FTP(servidor_ftp) as ftp:
        ftp.login(usuario, contraseña)
        
        nombre_archivo_descargar = seleccionar_archivo(ftp)
        ruta_archivo_local_descargar = f"/Users/diegi/Desktop/GS_DAM2/PSP/U4/U4A1/Program1/archivos_servidor/{nombre_archivo_descargar}"
        descargar_archivo(ftp, nombre_archivo_descargar, ruta_archivo_local_descargar)
        print(f"Archivo '{nombre_archivo_descargar}' descargado exitosamente.")

        print("Por favor, seleccione el archivo que desea cargar al servidor FTP.")
        ruta_archivo_local_cargar = seleccionar_archivo_local()
        nombre_archivo_cargar = ruta_archivo_local_cargar.split("/")[-1]
        cargar_archivo(ftp, nombre_archivo_cargar, ruta_archivo_local_cargar)
        print(f"Archivo '{nombre_archivo_cargar}' cargado exitosamente.")

if __name__ == "__main__":
    main()
