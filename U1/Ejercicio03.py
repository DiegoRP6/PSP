#Ejercicio 3: enumerar todos los procesos en el sistema operativo con PID y permitir 
#la terminación de uno mediante PID
import psutil
import multiprocessing

def list_processes():
    for process in psutil.process_iter(attrs=['pid', 'name']): #attrs=[] sirve para obtener esos parametros
        info = process.info
        print(f"El proceso {info['name']} con pid {info['pid']}")

def stop_process(pid):
    process = psutil.Process(pid)
    process.kill()
    print(f"El proceso {pid} ha sido terminado")

if __name__ == '__main__':
    list_processes()
    process_to_stop = int(input("Escribe el PID del proceso que quieres terminar"))

    stop_process(process_to_stop)

