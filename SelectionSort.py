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

def plot_graph(x, y1, y2, y3):
    plt.plot(x, y1, marker='o', color='red', label='Crescente')
    plt.plot(x, y2, marker='o', color='blue', label='Decrescente')
    plt.plot(x, y3, marker='o', color='green', label='Aleatório')
    plt.title("Análise de tempo de execução dos algoritmos de ordenação")
    plt.xlabel("Tamanho do vetor")
    plt.ylabel("Tempo (segundos)")
    plt.legend()
    plt.show()

def print_execution_time(time, sort_func_name, size):
    print(f"Tempo de execução para vetor de tamanho {size}: {time:.6f} segundos")

def run_sorting_analysis(array_sizes):
    sort_functions = {
        "Crescente": selection_sort,
        "Decrescente": lambda arr: selection_sort(arr[::-1]),
        "Aleatório": selection_sort
    }

    analysis_results = {}  # Dicionário para armazenar os tempos de execução

    merge_times = []
    reverse_times = []
    random_times = []

    for size in array_sizes:
        array = list(range(size))
        reverse_array = list(range(size, 0, -1))
        random_array = generate_random_array(size)

        merge_time = measure_execution_time(selection_sort.__name__, array)
        reverse_time = measure_execution_time(selection_sort.__name__, reverse_array)
        random_time = measure_execution_time(selection_sort.__name__, random_array)

        merge_times.append(merge_time)
        reverse_times.append(reverse_time)
        random_times.append(random_time)

        print_execution_time(merge_time, selection_sort.__name__, size)
        print_execution_time(reverse_time, selection_sort.__name__, size)
        print_execution_time(random_time, selection_sort.__name__, size)

    analysis_results["Crescente"] = merge_times
    analysis_results["Decrescente"] = reverse_times
    analysis_results["Aleatório"] = random_times

    plot_graph(array_sizes, merge_times, reverse_times, random_times)

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
