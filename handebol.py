num_jogadores, num_partidas = [int(i) for i in input().split()]

gols_todas_partidas = 0
for i in range(num_jogadores):
    gols = [int(i) for i in input().split()]

    num_gols = 0
    for j in gols:
        if j > 0:
            num_gols += 1
    
    if num_gols == num_partidas:
        gols_todas_partidas += 1

print(gols_todas_partidas)