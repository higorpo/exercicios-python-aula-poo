num_fileiras = int(input())
cores_fileira = [int(i) for i in input().split()]

linhas = []
linhas.append([*cores_fileira])

for i in range(1, num_fileiras):
    novaLinha = []

    for j, cor_bola in enumerate(linhas[i - 1]):
        # -1 1 1 -1 1
        if j == 0:
            continue
        
        if cor_bola != linhas[i-1][j-1]:
            novaLinha.append(-1)
        else:
            novaLinha.append(1)

    linhas.append([*novaLinha])


if linhas[-1][0] == 1:
    print('preta')
else:
    print('branca')