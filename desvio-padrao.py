import statistics

n = int(input())

numeros = []

for i in range(n):
    numeros.append(float(input()))

print(statistics.stdev(numeros))