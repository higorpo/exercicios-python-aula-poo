notas = [float(i) for i in input().split()]

del notas[notas.index(max(notas))]
del notas[notas.index(min(notas))]

print('{:.1f}'.format(sum(notas)))