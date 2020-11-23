crescente = False
decrescente = False
nao_ordenado = False

cartas = [int(i) for i in input().split()]

# Verifica se as cartas estão de forma crescente
for index, carta in enumerate(cartas):
    if index == 0:
        continue

    if carta > cartas[index - 1]:
        crescente = True
    else:
        crescente = False
        break

if crescente:
    print('C')
else:
    # Verifica se as cartas estão de forma decrescente
    for index, carta in enumerate(cartas):
        if index == 0:
            continue
        
        if cartas[index - 1] > carta:
            decrescente = True
        else:
            decrescente = False
            break

    if decrescente:
        print('D')
    else:
        print('N')
