import random

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        min_idx = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Uso 
tamanho = int(input("Digite o tamanho do vetor: "))
vetor = [random.randint(1, 100) for _ in range(tamanho)]

print("Vetor original:", vetor)

resultado = selection_sort(vetor)
print("Vetor ordenado:", resultado)
