import multiprocessing

def calcular_cuadrado(number, result):
    result.put(number * number)

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    resultado = multiprocessing.Queue()

    procesos = []
    for num in numeros:
        proceso = multiprocessing.Process(target=calcular_cuadrado, args=(num, resultado))
        procesos.append(proceso)
        proceso.start()

    for proceso in procesos:
        proceso.join()

    resultados = []
    while not resultado.empty():
            resultados.append(resultado.get())

    print("Resultados", resultados)