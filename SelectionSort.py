import random
import timeit
import matplotlib.pyplot as plt

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def measure_execution_time(sort_func, array):
    setup_code = f"from __main__ import {sort_func}"
    stmt = f"{sort_func}({array})"
    time = timeit.timeit(stmt=stmt, setup=setup_code, number=1)
    return time

def plot_graph(x, y, title):
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.xlabel("Tamanho do vetor")
    plt.ylabel("Tempo (segundos)")
    plt.show()

def print_execution_time(time, sort_func_name, size):
    print(f"Tempo de execução para vetor de tamanho {size}: {time:.6f} segundos")

def run_sorting_analysis(array_sizes):
    sort_functions = {"Crescente": selection_sort,
                      "Decrescente": selection_sort,
                      "Aleatório": selection_sort}

    analysis_results = {}  # Dicionário para armazenar os tempos de execução

    for title, sort_func in sort_functions.items():
        execution_times = []
        for size in array_sizes:
            array = generate_random_array(size) if title == "Aleatório" else list(range(size))
            time = measure_execution_time(sort_func.__name__, array)
            execution_times.append(time)
            print_execution_time(time, sort_func.__name__, size)

        analysis_results[title] = execution_times  # Armazena os tempos de execução correspondentes

        plot_graph(array_sizes, execution_times, f"Análise de tempo - {title}")

    # Imprime a análise correspondente aos tempos de execução
    for title, execution_times in analysis_results.items():
        print(f"\nAnálise correspondente a {title}:")
        min_time = min(execution_times)
        max_time = max(execution_times)
        avg_time = sum(execution_times) / len(execution_times)
        print(f"Mínimo: {min_time:.6f} segundos")
        print(f"Máximo: {max_time:.6f} segundos")
        print(f"Média: {avg_time:.6f} segundos")


array_sizes = [50, 500, 5000, 50000]
run_sorting_analysis(array_sizes)
