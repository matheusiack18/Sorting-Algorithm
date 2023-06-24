import random # Importa a biblioteca random que serve para gerar numeros aleatorios;
import timeit # Importa a biblioteca timeit que serve para medir o tempo de execucao;
import matplotlib.pyplot as plt # Serve para plotar o grafico;

# Implementacao do algoritmo de ordencao, A funcao a seguir vai dividir a lista em sublistas, depois vai ordenar cada sublista e em seguida mescar as sublistas;
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2
    esq = arr[:meio]
    direi = arr[meio:]

    esq = merge_sort(esq)
    direi = merge_sort(direi)

    return merge(esq, direi)

# A funcao a seguir e responsavel por mesclar as duas sublistas ordenadas em uma unica lista ordenada 
def merge(esq, direi):
    merged = []
    esq_index = 0
    direi_index = 0

    while esq_index < len(esq) and direi_index < len(direi):
        if esq[esq_index] <= direi[direi_index]:
            merged.append(esq[esq_index])
            esq_index += 1
        else:
            merged.append(direi[direi_index])
            direi_index += 1

    while esq_index < len(esq):
        merged.append(esq[esq_index])
        esq_index += 1

    while direi_index < len(direi):
        merged.append(direi[direi_index])
        direi_index += 1

    return merged

# Gera o vetores aleatorios para tamanhos diferentes e gera numeros aleatorios de 0 ate 50000;
def generate_random_array(size):
    return [random.randint(0, 50000) for _ in range(size)]

# Mede o tempo de execucao de uma funcao de ordenacao para um determinado vetor, e utilizamos a funcao da biblioteca timeit para medir o tempo em segundos;
def measure_execution_time(sort_func, array):
    time = timeit.timeit(lambda: sort_func(array), number=1)
    return time

# A partir dessa linha e a funcao que plota o grafico com os tempos de execucoes para determinados tamanhos de vetores;
def plot_graph(x, y1, y2, y3):
    plt.plot(x, y1, marker='x', color='red', label='Crescente')
    plt.plot(x, y2, marker='x', color='blue', label='Decrescente')
    plt.plot(x, y3, marker='x', color='green', label='Aleatório')
    plt.title("Análise de tempo de execução dos algoritmos de ordenação")
    plt.xlabel("Tamanho do vetor")
    plt.ylabel("Tempo (segundos)")
    plt.legend()
    plt.show()
# A funcao que plota o grafico vai ate a linha anterior, e utilizamos a biblioteca matplotlib.pyplot para criar o grafico;

# Imprime o tempo de execução de um algoritmo de ordenação para uma determinada lista;
def print_execution_time(time, sort_func_name, size):
    print(f"Tempo de execução para vetor de tamanho {size}: {time:.6f} segundos")

# A funca realiza a análise de tempo de execução dos algoritmos de ordenação. 
# E a funcao 'sort_functions' cria um dicionario que mapeia os diferentes tipos de lista para as funcoes correspondentes;
def run_sorting_analysis(array_sizes):
    sort_functions = {
        "Crescente": lambda arr: merge_sort(arr),
        "Decrescente": lambda arr: merge_sort(arr[::-1]),
        "Aleatório": merge_sort
    }

    analysis_results = {}  # Dicionário para armazenar os tempos de execução

    merge_times = [] # Ordem Crescente
    reverse_times = [] # Ordem Decrescente
    random_times = [] # Ordem Aleatoria 

    for size in array_sizes:
        array = list(range(size))
        reverse_array = list(range(size, 0, -1))
        random_array = generate_random_array(size)

        # Depois dessa linha vai medir o tempo de execucao para cada caso usando as funcoes a seguir que e a 'measure_execution_time';
        merge_time = measure_execution_time(merge_sort, array)
        reverse_time = measure_execution_time(merge_sort, reverse_array)
        random_time = measure_execution_time(merge_sort, random_array)

        # E adiciona os tempos a lista correspondente;
        merge_times.append(merge_time)
        reverse_times.append(reverse_time)
        random_times.append(random_time)

        # Imprime os tempos de execucao para cada caso e tamanho do vetor;
        print_execution_time(merge_time, merge_sort.__name__, size)
        print_execution_time(reverse_time, merge_sort.__name__, size)
        print_execution_time(random_time, merge_sort.__name__, size)

    # Armazena os tempos de execucao no dicionario 'analysis_results' para os casos;
    analysis_results["Crescente"] = merge_times
    analysis_results["Decrescente"] = reverse_times
    analysis_results["Aleatório"] = random_times

    # Plota o grafico com os tempos de execucao para os casos e vetores diferentes;
    plot_graph(array_sizes, merge_times, reverse_times, random_times)

    # Imprime a análise correspondente aos tempos de execução
    for title, execution_times in analysis_results.items():
        print(f"\nAnálise correspondente a {title}:")
        min_time = min(execution_times)
        max_time = max(execution_times)

        print(f"Mínimo: {min_time:.6f} segundos")
        print(f"Máximo: {max_time:.6f} segundos")

        
print("\n")

# As linhas a seguir definem os tamanhos dos vetores a serem analisados e chamam a funcao para executar a analise de tempo de execucao; 
array_sizes = [50, 500, 5000, 50000]
run_sorting_analysis(array_sizes)
