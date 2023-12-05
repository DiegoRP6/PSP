import multiprocessing
import time
import os

# Lista de nombres de archivos para procesar
archivos = ["archivo1.txt", "archivo2.txt", "archivo3.txt"]

# Directorio de origen para los archivos
source_dir = "/path/to/source/files/"

# Directorio de destino para los resultados
destination_dir = "/path/to/destination/files/"

def procesar_archivo(archivo, lock):
    # Simulación de procesamiento del archivo
    time.sleep(2)

    # Sección crítica: mover el archivo a la carpeta de destino sin utilizar lock
    lock.acquire()
    source_path = os.path.join(source_dir, archivo)
    destination_path = os.path.join(destination_dir, archivo)
    os.rename(source_path, destination_path)
    print(f"{archivo} procesado y movido a {destination_dir}")
    lock.release()

if __name__ == "__main__":
    # Utilizar un Manager para crear un Lock compartido entre procesos
    lock = multiprocessing.Lock()

        # Crear procesos para procesar archivos en paralelo
    procesos = []
    for archivo in archivos:
        proceso = multiprocessing.Process(target=procesar_archivo, args=(archivo, lock))
        procesos.append(proceso)
        proceso.start()
    # Esperar a que todos los procesos terminen
    for proceso in procesos:
        proceso.join()
    # Imprimir mensaje de finalización
    print("Procesamiento de archivos completado.")