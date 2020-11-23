casos_teste = int(input())

for i in range(casos_teste):
    ganhador_index = None
    menor_diferenca = 9999999999999

    alunos, numero_sorteado = [int(z) for z in input().split()]
    
    numeros_chutados = [int(z) for z in input().split()]
    
    for index, numero_chutado in enumerate(numeros_chutados):
        if abs(numero_sorteado - numero_chutado) < menor_diferenca:
            menor_diferenca = abs(numero_sorteado - numero_chutado)
            ganhador_index = index

    print(ganhador_index + 1)