import random
import timeit
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def measure_execution_time(sort_func, array):
    time = timeit.timeit(lambda: sort_func(array), number=1)
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
    sort_functions = {
        "Crescente": lambda arr: merge_sort(arr),
        "Decrescente": lambda arr: merge_sort(arr[::-1]),
        "Aleatório": merge_sort
    }

    analysis_results = {}  # Dicionário para armazenar os tempos de execução

    for title, sort_func in sort_functions.items():
        execution_times = []
        for size in array_sizes:
            array = generate_random_array(size) if title == "Aleatório" else list(range(size))
            time = measure_execution_time(sort_func, array)
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
