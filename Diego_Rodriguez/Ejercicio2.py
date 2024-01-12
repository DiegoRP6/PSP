#EJERCICIO2(2,5puntos)
#dado el siguiente código hazlo multihilo(0,5 puntos), consigue que la información pueda aparecer ordenada 
#por pantalla y en el fichero se escriba de manera ordenada(2 puntos)

import os, psutil, time, subprocess, multiprocessing, sys
import threading
import tempfile

file_name = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())

def code(name, lock):
    time.sleep(10)
    with open(file_name, 'w') as f:
        lock.acquire()
        print("guardando en "+file_name)
        f.write("codigo limpio fue escrito por "+str(name))
    subprocess.run(["ping", "google.com", "-n", "4"])
    lock.release()

# llama a al metodo code usando hilos
lock = threading.Lock()
h = threading.Thread(target=code , args=("Diego", lock,))
h.start()

h1 = threading.Thread(target=code , args=("Diego", lock,))
h1.start()

h2 = threading.Thread(target=code , args=("Diego", lock,))
h2.start()

h3 = threading.Thread(target=code , args=("Diego", lock,))
h3.start()

h4 = threading.Thread(target=code , args=("Diego", lock,))
h4.start()

h.join()
h1.join()
h2.join()
h3.join()
h4.join()
