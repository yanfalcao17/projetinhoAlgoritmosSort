from operator import le
from mergeSort import merge_sort
from mergeSort3way import merge_sort_3_way
import projetinhoExec
import time

entradas = projetinhoExec.gerar_entradas()
tamanho_entradas = len(entradas)
#print(entradas)
#print(tamanho_entradas)

for i in range(tamanho_entradas):
    start_time = time.time()
    merge_sort(entradas[i], 0, len(entradas[i])-1)
    #print(entradas[i])
    print(len(entradas[i]))
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    merge_sort_3_way(entradas[i])
    #print(entradas[i])
    print("--- %s seconds ---" % (time.time() - start_time))