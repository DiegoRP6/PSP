
import queue
import threading
import time
import random

q = queue.Queue()

class Productor(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        while True:
            a = self.q.put(1)
            b = self.q.put(2)
            time.sleep(1)
            print("Contenido de la cola: "+str(list(self.q.queue)))


class Consumidor(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        while True:
            a = self.q.get()
            b = self.q.get()
            sum = a + b
            print(sum)
            time.sleep(2) 

p = Productor(q)
c = Consumidor(q)

p.start()
c.start()

p.join()
c.join()



