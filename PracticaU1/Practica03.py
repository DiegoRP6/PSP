#Suma de Listas en Paralelo:
import multiprocessing

def suma_list(sub_list):
    result = sum(sub_list)
    print(f"{result}")

if __name__ == '__main__':
    number_list = [1, 5, 19, 30, 42, 2, 67, 20, 30, 40]
    pool_size = 4
    size_sub_list = len(number_list) // pool_size
    processes = []

    for process in range(pool_size):
        start = process * size_sub_list
        finish = (process + 1) * size_sub_list if process < pool_size - 1 else len(number_list)
        sub_list = number_list[start:finish]
        process = multiprocessing.Process(target=suma_list, args=(sub_list,))
        process.start()
        processes.append(process)

    resultados = []
    for proces in processes:
        proces.join()