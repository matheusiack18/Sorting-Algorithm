# Neste arquivo e pra ser feito a analise com vetores de numeros inteiros de tamanhos 50, 500, 5000, 50000;

import random

def merge_sort(array):
    if len(array) <= 1:
        return array

    meio = len(array) // 2
    ladoesquerdo = array[:meio]
    ladodireito = array[meio:]

    ladoesquerdo = merge_sort(ladoesquerdo)
    ladodireito = merge_sort(ladodireito)

    return merge(ladoesquerdo, ladodireito)


def merge(esquerda, direita):
    merged = []
    numesq = numdir = 0

    while numesq < len(esquerda) and numdir < len(direita):
        if esquerda[numesq] < direita[numdir]:
            merged.append(esquerda[numesq])
            numesq += 1
        else:
            merged.append(direita[numdir])
            numdir += 1

    while numesq < len(esquerda):
        merged.append(esquerda[numesq])
        numesq += 1

    while numdir < len(direita):
        merged.append(direita[numdir])
        numdir += 1

    return merged