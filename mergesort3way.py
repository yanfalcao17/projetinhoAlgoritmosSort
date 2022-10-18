# mergesort dividido em 3 partes.


def merge(lista, inicio, meio1, meio2, fim):

    lista_esquerda = lista[inicio -1 : meio1]
    lista_meio = lista[meio1: meio2 + 1]
    lista_direita = lista[meio2 + 1 : fim]

    lista_esquerda.append(float('inf'))
    lista_meio.append(float('inf'))
    lista_direita.append(float('inf'))
    
    index_esquerdo = 0
    index_meio = 0
    index_direita = 0
    for i in range(inicio-1, fim):
        minimum = min([lista_esquerda[index_esquerdo], lista_meio[index_meio], lista_direita[index_direita]])
        if minimum == lista_esquerda[index_esquerdo]:
            lista[i] = lista_esquerda[index_esquerdo]
            index_esquerdo += 1
        elif minimum == lista_meio[index_meio]:
            lista[i] = lista_meio[index_meio]
            index_meio += 1
        else:
            lista[i] = lista_direita[index_direita]
            index_direita += 1
            
def merge_sort_3(lista, inicio, fim):

    if len(lista[inicio -1: fim]) < 2:
        return lista
    else: 
        meio1 = inicio + ((fim - inicio) // 3)
        meio2 = inicio + 2 * ((fim-inicio) // 3)

        merge_sort_3(lista, inicio, meio1)
        merge_sort_3(lista, meio1+1, meio2 + 1)
        merge_sort_3(lista, meio2+2, fim)
        merge(lista, inicio, meio1, meio2, fim)
        return lista
