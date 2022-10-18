from operator import le
from mergeSort import merge_sort
from mergesort3way import merge_sort_3
import projetinhoExec
import time

entradas = projetinhoExec.gerar_entradas()
tamanho_entradas = len(entradas)
print(entradas)
print(tamanho_entradas)

for i in range(tamanho_entradas):
    start_time = time.time()
    merge_sort(entradas[i], 0, len(entradas[i])-1)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(len(entradas[i]))

    start_time = time.time()
    merge_sort_3(entradas[i], 0, len(entradas[i])-1)
    print("--- %s seconds ---" % (time.time() - start_time))