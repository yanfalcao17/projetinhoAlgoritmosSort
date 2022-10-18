# implementação do merge

def merge(lista,esquerda,direita,meio):
    if esquerda==meio==direita:
        return
    a=[0]*(meio-esquerda+1)
    b=[0]*(direita-meio)
    for i in range(0,meio-esquerda+1):
        a[i]=lista[i+esquerda]
    for i in range(0,direita-meio):
        b[i]=lista[i+meio+1]
    k=esquerda
    j=0
    for i in range(0,len(a)):
        while j < len(b) and a[i] > b[j]:
            lista[k]=b[j]
            j=j+1
            k=k+1
        lista[k]=a[i]
        k=k+1
    while j < len(b) :
        lista[k]=b[j]
        j=j+1
        k=k+1

# implementação do mergesort

def merge_sort(lista,esquerda,direita):
    meio=esquerda + round((direita - esquerda)/2)
    if direita==esquerda:
        return
    elif (direita-esquerda)==1:
        merge(lista, esquerda, direita, meio)
    else:
        merge_sort(lista,esquerda,meio)
        merge_sort(lista,meio+1,direita)
    merge(lista,esquerda,direita,meio)