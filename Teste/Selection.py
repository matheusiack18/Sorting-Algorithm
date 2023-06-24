import random # Importa a biblioteca random que serve para gerar numeros aleatorios;
import timeit # Importa a biblioteca timeit que serve para medir o tempo de execucao;
import matplotlib.pyplot as plt # Serve para plotar o grafico;

# Implementacao do algoritmo de ordenacao, que recebe um array como entrada e retorna o array ordenado;
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Gera o vetores aleatorios para tamanhos diferentes e gera numeros aleatorios de 0 ate 50000;
def generate_random_array(size):
    return [random.randint(0, 50000) for _ in range(size)]

# Mede o tempo de execucao de uma funcao de ordenacao para um determinado vetor, e utilizamos a funcao da biblioteca timeit para medir o tempo em segundos;
def measure_execution_time(sort_func, array):
    setup_code = f"from __main__ import {sort_func}"
    stmt = f"{sort_func}({array})"
    time = timeit.timeit(stmt=stmt, setup=setup_code, number=1)
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

# Essa funcao serve para imprimir o tempo de execucao de um determinado vetor em casos diferentes ela recebe o tempo de execucao, o nome da funcao de ordenacao
# e o tamanho do vetor como parametros;
def print_execution_time(time, sort_func_name, size):
    print(f"Tempo de execução para vetor de tamanho {size}: {time:.6f} segundos")

# Executa as analises de tempo de execucao, ela recebe uma lista de tamanhos de vetor como parametro;
def run_sorting_analysis(array_sizes):
# O sort_functions e o dicionario que vai ser responsavel por mapear cada caso diferente sendo eles o de ordem crescente, decrescente e aleatorio);
    sort_functions = {
        "Crescente": selection_sort,
        "Decrescente": lambda arr: selection_sort(arr[::-1]),
        "Aleatório": selection_sort
    }

    # As linhas a seguir inicializam um dicionario vazio com a funcao de armazenar os tempos de execucao; 
    analysis_results = {}

    # E as tres listas vazias servem para armazenar os tempos de execucao de cada caso; 
    selection_times = []
    reverse_times = []
    random_times = []

    # A partir dessa linha para cada tamanho de vetor vai ser realizado a geracao dos vetores em cada ordem;
    for size in array_sizes:
        array = list(range(size))
        reverse_array = list(range(size, 0, -1))
        random_array = generate_random_array(size)

        # Depois dessa linha vai medir o tempo de execucao para cada caso usando as funcoes a seguir que e a 'measure_execution_time';
        selection_time = measure_execution_time(selection_sort.__name__, array)
        reverse_time = measure_execution_time(selection_sort.__name__, reverse_array)
        random_time = measure_execution_time(selection_sort.__name__, random_array)

        #  E adiciona os tempos a lista correspondente;
        selection_times.append(selection_time)
        reverse_times.append(reverse_time)
        random_times.append(random_time)

        # Imprime os tempos de execucao para cada caso e tamanho do vetor;
        print_execution_time(selection_time, selection_sort.__name__, size)
        print_execution_time(reverse_time, selection_sort.__name__, size)
        print_execution_time(random_time, selection_sort.__name__, size)

    # Armazena os tempos de execucao no dicionario 'analysis_results' para os casos;
    analysis_results["Crescente"] = selection_times
    analysis_results["Decrescente"] = reverse_times
    analysis_results["Aleatório"] = random_times

    # Plota o grafico com os tempos de execucao para os casos e vetores diferentes;
    plot_graph(array_sizes, selection_times, reverse_times, random_times)

    # Imprime a análise correspondente aos tempos de execução e tambem tem o menor tempo de execucao e o maximo;
    for title, execution_times in analysis_results.items():
        print(f"\nAnálise correspondente a {title}:")
        min_time = min(execution_times)
        max_time = max(execution_times)

        print(f"Mínimo: {min_time:.6f} segundos")
        print(f"Máximo: {max_time:.6f} segundos")

print("\n")
# As linhas a seguir definem os tamanhos dos vetores a serem analisados e chamam a funcao para executar a analise de tempo de execucao; 
array_sizes = [50, 500]
run_sorting_analysis(array_sizes)

# Observacao: 
# A funcao 'lambda' no python e é usado para criar funções anônimas de forma concisa e inline, especialmente em situações em que uma função simples 
# e de curta duração é necessária.No caso do seu código, ele é usado para definir a função de ordenação para o caso "Decrescente" 
# sem a necessidade de criar uma função separada com um nome associado a ela.