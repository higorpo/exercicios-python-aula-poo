# Dada um sequência de números inteiros, determine o menor destes valores.
# Nos dados de entrada, o primeiro valor indica o tamanho da sequência, ou seja,
# ele é seguido por esta quantidade de valores, como no exemplo abaixo no que o primeiro valor é 4,
# indicando que após ele vejam a sequência de quatro valores inteiros.

import math

tamanhoSeq = int(input())

sequencia = []
for i in range(tamanhoSeq):
    sequencia.append(int(input()))

menorValor = math.inf

for valor in sequencia:
    if valor < menorValor:
        menorValor = valor
        
print(menorValor)