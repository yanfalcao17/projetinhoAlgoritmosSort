import random
# gera valores pseudo aleatorios

def criar_lista_aleatoria(n):
    lista = []
    for _ in range(n):
        lista.append(random.uniform(-(2*(n)),(2*(n))))
    return lista

def gerar_tamanho_lista():
    n = random.randint(10,10000)
    return n

def numero_de_entradas():
    n = random.randint(10,20)
    return n

def gerar_entradas():
    
    lista = []
    n = numero_de_entradas()
    for i in range(n):
        tamanho = gerar_tamanho_lista()
        lista.append(criar_lista_aleatoria(tamanho))
        print(tamanho)
    
    print(n)
    return lista




