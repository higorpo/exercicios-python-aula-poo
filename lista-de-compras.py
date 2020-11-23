casos_de_teste = int(input())

for i in range(casos_de_teste):
    lista_de_compras = []
    lista = [i for i in input().split()]
    print(' '.join(sorted(set(lista))))