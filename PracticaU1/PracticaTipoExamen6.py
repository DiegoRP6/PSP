import multiprocessing
import time
import os

# Lista de URLs de archivos para descargar
urls = ["https://example.com/file1.txt", "https://example.com/file2.txt", "https://example.com/file3.txt"]

# Directorio de destino para los archivos descargados
download_dir = "/path/to/downloaded/files/"

# Archivo compartido donde se escribirá el contenido descargado
shared_file = "/path/to/shared/file.txt"

def descargar_archivo(url, lock):
    # Simulación de la descarga del archivo
    time.sleep(2)
    lock.acquire()
    with open(shared_file, 'a') as f:
        f.write(f"Contenido de {url}\n")
    lock.release()

if __name__ == "__main__":
    
    lock = multiprocessing.Lock()

    # Crear procesos para descargar archivos en paralelo
    procesos = []
    for url in urls:
        proceso = multiprocessing.Process(target=descargar_archivo, args=(url, lock,))
        procesos.append(proceso)
        proceso.start()

    # Esperar a que todos los procesos terminen
    for proceso in procesos:
        proceso.join()

    # Imprimir mensaje de finalización
    print("Descargas completadas. Contenido de los archivos guardado en", shared_file)