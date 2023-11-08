#Cálculo de Factoriales en Paralelo:


import multiprocessing

def get_factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    print(f"El factorial de {num} es {result}")

if __name__ == '__main__':
    numbers = [6, 12, 19]
    processes = []

    for number in numbers:
        process = multiprocessing.Process(target=get_factorial, args=(number,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

