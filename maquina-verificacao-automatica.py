conectorA = [int(i) for i in input().split()]
conectorB = [int(i) for i in input().split()]

valido = True

for a, b in zip(conectorA, conectorB):
    if a == b:
        valido = False
        break

print('Y' if valido else 'N')