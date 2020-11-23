qtdLista1 = int(input())

nomes1 = []

for i in range(qtdLista1):
    nomes1.append(input())

qtdLista2 = int(input())

nomes2 = []

for i in range(qtdLista2):
    nomes2.append(input())

nomes = nomes1 + nomes2

for nome in sorted(nomes):
    print(nome)