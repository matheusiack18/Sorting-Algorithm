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
    time = timeit.timeit(lambda: sort_func(array), number=1)
    return time

def plot_graph(x, y1, y2):
    plt.plot(x, y1, marker='o', color='red', label='Merge Sort')
    plt.plot(x, y2, marker='o', color='blue', label='Selection Sort')
    plt.title("Comparação de tempo de execução")
    plt.xlabel("Tamanho do vetor")
    plt.ylabel("Tempo (segundos)")
    plt.legend()
    plt.show()

def print_execution_time(time, sort_func_name, size):
    print(f"Tempo de execução para vetor de tamanho {size}: {time:.6f} segundos")

def run_sorting_analysis(array_sizes):
    sort_functions = {
        "Crescente": [merge_sort, selection_sort],
        "Decrescente": [merge_sort, selection_sort],
        "Aleatório": [merge_sort, selection_sort]
    }

    analysis_results = {}  # Dicionário para armazenar os tempos de execução

    for title, sort_funcs in sort_functions.items():
        merge_sort_func, selection_sort_func = sort_funcs
        merge_execution_times = []
        selection_execution_times = []

        for size in array_sizes:
            array = generate_random_array(size) if title == "Aleatório" else list(range(size))

            merge_time = measure_execution_time(merge_sort_func, array)
            selection_time = measure_execution_time(selection_sort_func, array)

            merge_execution_times.append(merge_time)
            selection_execution_times.append(selection_time)

            print_execution_time(merge_time, merge_sort_func.__name__, size)
            print_execution_time(selection_time, selection_sort_func.__name__, size)

        analysis_results[title] = {
            "- Merge Sort": merge_execution_times,
            "- Selection Sort": selection_execution_times
        }  # Armazena os tempos de execução correspondentes

        plot_graph(array_sizes, merge_execution_times, selection_execution_times)

    # Imprime a análise correspondente aos tempos de execução
    for title, execution_times in analysis_results.items():
        print(f"\nAnálise correspondente a {title}:")
        for sort_func_name, times in execution_times.items():
            min_time = min(times)
            max_time = max(times)
            avg_time = sum(times) / len(times)
            print(f"{sort_func_name}:")
            print(f"Mínimo: {min_time:.6f} segundos")
            print(f"Máximo: {max_time:.6f} segundos")
            print(f"Média: {avg_time:.6f} segundos")

array_sizes = [50, 500, 5000, 50000]
run_sorting_analysis(array_sizes)
