#Exercise 3: 
#Cree un hilo que genere números aleatorios entre 1 y 100 y los vaya insertando en una lista, 
#y otro que recorra circularmente esa lista y sustituya los números terminados en cero por el valor -1. 
#Un tercer hilo abortará los otros dos en el momento en el que la suma de los elementos de la lista 
#supere el valor de 20000

import random
import threading
import time
import sys

def generate_numbers(lst, stop_event):
    while not stop_event.is_set():
        number = random.randint(1, 100)
        lst.append(number)

def replace_numbers(lst, stop_event):
    index = 0
    while not stop_event.is_set():
        if lst[index] % 10 == 0:
            lst[index] = -1
        time.sleep(0.1)

def stop_threads(lst, stop_event):
    while not stop_event.is_set():
        if sum(lst) > 20000:
            stop_event.set()
            print(f"Lista: {lst}")
            print("Ya ha llegado a los 20000")
            sys.exit()

if __name__ == "__main__":
    my_list = []
    threads = []
    stop_event = threading.Event()

    generate_thread = threading.Thread(target=generate_numbers, args=(my_list, stop_event))
    replace_thread = threading.Thread(target=replace_numbers, args=(my_list, stop_event))
    stop_thread = threading.Thread(target=stop_threads, args=(my_list, stop_event))

    threads.append(generate_thread)
    threads.append(replace_thread)
    threads.append(stop_thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()