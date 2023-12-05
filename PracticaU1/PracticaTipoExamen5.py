import os, psutil, time, subprocess, multiprocessing, sys
import threading
import tempfile
file_name = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
   
def mimetodo(nota):
# Open the file for writing.
    time.sleep(1)
    lock.acquire()
    subprocess.run(["ping", "google.com"])
    time.sleep(1)

    with open(file_name, 'w') as f:
        print("guardando en "+file_name)
        f.write("mi nota del examen es un "+str(nota))
    lock.release()

# llama  a mi metodo usando hilos
lock = threading.Lock()
h = threading.Thread(target=mimetodo, args=(10,))
h.start()

h1 = threading.Thread(target=mimetodo, args=(10,))
h1.start()

h2 = threading.Thread(target=mimetodo, args=(10,))
h2.start()

h3 = threading.Thread(target=mimetodo, args=(10,))
h3.start()

h4 = threading.Thread(target=mimetodo, args=(10,))
h4.start()

h.join()
h1.join()
h2.join()
h3.join()
h4.join()