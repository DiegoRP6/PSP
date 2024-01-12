#EJERCICIO3(3 puntos + 0,5opcional)
#Usando procesos, abre tres procesos,cada uno de los cuales debe….
#	P1: debe abrir el bloc de notas/editor de texto del sistema que uses
#	P2: debes esperar 5 segundos para cambiar la prioridad de P1
#	P3: se lanza 2 segundos después de P2 y mata a P1 al instante
#	¿Qué es lo que ocurre durante la ejecución?¿Termina el programa correctamente?¿Cómo podrías solucionarlo?
#OPCIONAL +0,5: ¿Qué mecanismo de los estudiados te permitiría sincronizar la muerte de P1?Describe  todo lo 
#que se te ocurra al respecto 
import os, psutil, time, subprocess, multiprocessing

def abrir_notas():
    p = subprocess.Popen(["notepad.exe"])
    print("PID:", p.pid, "Abriendo bloc de notas")
    return p.pid

def cambiar_prioridad(pid):
    p = psutil.Process(pid)
    p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    print("PID:", pid, "Prioridad cambiada")

def matar_proceso(pid):
    p = psutil.Process(pid)
    p.kill()
    print("PID:", pid, "Bloc de notas muerto")

if __name__ == "__main__":
    pid = abrir_notas()

    # P1: Cambiar prioridad después de 5 segundos
    time.sleep(5)
    p1 = multiprocessing.Process(target=cambiar_prioridad, args=(pid,))
    p1.start()
    p1.join()

    # P2: Matar proceso después de 2 segundos
    time.sleep(2)
    p2 = multiprocessing.Process(target=matar_proceso, args=(pid,))
    p2.start()
    p2.join()