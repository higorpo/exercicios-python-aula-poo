# No último campeonato mundial de atletismo foram anotados as marcas dos 3 saltos em distância de cada um dos atletas,
# juntamente com seu nome. Imprima, então, o nome do primeiro colocado, considerando que o vencedor é o atleta com o melhor
# salto de todos.
# Os dados de entrada estão no formato exemplificado abaixo, sendo que na primeira linha há o número de saltadores.
# Nas n linhas subsequentes estão os dados dos saltadores, uma linha para cada saltador contendo as distâncias dos 3 saltos
# e o nome do saltador.

qtdSaltadores = int(input())

saltadores = []
maiorSaltoDoSaltador = []

for i in range(qtdSaltadores):
    saltos = []
    inputed = input().split()
    saltos.append(float(inputed[0]))
    saltos.append(float(inputed[1]))
    saltos.append(float(inputed[2]))
    saltador = inputed[3]
    maiorSaltoDoSaltador.append(sorted(saltos)[-1])
    saltadores.append(saltador)

maiorSaltoDoSaltadorIndex = maiorSaltoDoSaltador.index(sorted(maiorSaltoDoSaltador)[-1])

print(saltadores[maiorSaltoDoSaltadorIndex])