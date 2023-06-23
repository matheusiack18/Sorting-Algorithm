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
        "Crescente": lambda arr: merge_sort(arr),
        "Decrescente": lambda arr: merge_sort(arr[::-1]),
        "Aleatório": merge_sort
    }

    analysis_results = {}  # Dicionário para armazenar os tempos de execução

    merge_times = []
    reverse_times = []
    random_times = []

    for size in array_sizes:
        array = list(range(size))
        reverse_array = list(range(size, 0, -1))
        random_array = generate_random_array(size)

        merge_time = measure_execution_time(merge_sort, array)
        reverse_time = measure_execution_time(merge_sort, reverse_array)
        random_time = measure_execution_time(merge_sort, random_array)

        merge_times.append(merge_time)
        reverse_times.append(reverse_time)
        random_times.append(random_time)

        print_execution_time(merge_time, merge_sort.__name__, size)
        print_execution_time(reverse_time, merge_sort.__name__, size)
        print_execution_time(random_time, merge_sort.__name__, size)

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
