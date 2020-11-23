numero_postos_agua, distancia_inter_max = [int(i) for i in input().split()]
postos_agua_posicao = [int(i) for i in input().split()]

consegue_terminar = True

for i in range(numero_postos_agua):
    if i == 0:
        continue
    
    if postos_agua_posicao[i] - postos_agua_posicao[i - 1] > distancia_inter_max:
        consegue_terminar = False
        break

print('S' if consegue_terminar else 'N')