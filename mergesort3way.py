def merge_sort_3_way(lista):

    if len(lista) <= 1:
        return
    meio1 = len(lista)//3
    meio2 = 2*len(lista)//3
    esquerda, meio, direita = lista[:meio1], lista[meio1:meio2] , lista[meio2:]

    merge_sort_3_way(esquerda)
    merge_sort_3_way(meio)
    merge_sort_3_way(direita)
    temp = merge_3(esquerda, meio, direita)
    for i in range(len(temp)):
        lista[i] = temp[i]

def merge_3(esqueda, meio, direita):
    lista = []
    i = j = k = 0
    while i < len(esqueda) or k < len(direita) or j < len(meio):
        if i >= len(esqueda):
            lista = lista + merge(meio[j:],direita[k:])
            break
        elif j >= len(meio):
            lista = lista + merge(esqueda[i:],direita[k:])
            break
        elif k >= len(direita):
            lista = lista + merge(esqueda[i:],meio[j:])
            break
        else:
            if esqueda[i] >= meio[j]:
                if meio[j] >= direita[k]:
                    lista.append(direita[k])
                    k += 1
                else:
                    lista.append(meio[j])
                    j += 1
            else:
                if esqueda[i] >= direita[k]:
                    lista.append(direita[k])
                    k += 1
                else:
                    lista.append(esqueda[i])
                    i += 1
    return lista



def merge(esquerda, direita):
    lista = []
    i = j = 0
    while i < len(esquerda) or j < len(direita):
        if i >= len(esquerda):
            lista.append(direita[j])
            j += 1
        elif j >= len(direita):
            lista.append(esquerda[i])
            i += 1
        else:
            if esquerda[i] <= direita[j]:
                lista.append(esquerda[i])
                i += 1
            else:
                lista.append(direita[j])
                j+=1
    return lista