numeroPraias = int(input())

praias = []
distanciaPraias = []

for i in range(numeroPraias):
    praia, distancia = input().split(';')
    distancia = int(distancia)
    
    praias.append(praia)
    distanciaPraias.append(distancia)

praiasEntre10e20km = 0

for i in distanciaPraias:
    if i >= 15 and i <= 20:
        praiasEntre10e20km += 1

praiaMaisDistante = praias[distanciaPraias.index(sorted(distanciaPraias)[-1])]
mediaDistanciaPraias = sum(distanciaPraias) / float(len(distanciaPraias))

print('{};{};{:.1f}'.format(praiaMaisDistante, praiasEntre10e20km, mediaDistanciaPraias))