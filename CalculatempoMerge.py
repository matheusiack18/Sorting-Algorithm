import time
import random
from MergeSort import merge_sort



### EXERCÍCIO 1 ###

# Obter o tamanho do vetor a partir do usuário
tamanho = int(input("EXERCÍCIO 1 - Digite o tamanho do vetor: "))

# Obter os elementos do vetor a partir do usuário
vetor = [i for i in range(tamanho)]

tempo_inicio_crescente = time.time()

vetor_crescente_ordenado = merge_sort(vetor)

print('\nTempo levado para executar: ' + str(time.time() - tempo_inicio_crescente))

#############################################################################################################################
### EXERCÍCIO 2 ###




#############################################################################################################################
### EXERCÍCIO 4 ###
# Obter o tamanho do vetor a partir do usuário
tamanho = int(input("\nEXERCÍCIO 4 - Digite o tamanho do vetor: "))

# Gerar um vetor com números aleatórios
vetor = [random.randint(1, 90000) for _ in range(tamanho)]


start_time = time.time()

# Imprimir o vetor original
# print("Vetor original:", vetor)

# Ordenar o vetor usando o Merge Sort
vetor_ordenado = merge_sort(vetor)

# Imprimir o vetor ordenado
# print("\nVetor ordenado:", vetor_ordenado)

print('\nTempo levado para executar: ' + str(time.time() - start_time))
