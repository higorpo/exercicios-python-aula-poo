# Calcular quanto tempo demora a massa de um material radioativo para reduzir a menos de 0,5 gramas, dado que um material radioativo perde metade de sua massa a cada 50 segundos. O valor de entrada é um número real correspondente à massa. A saída é um número inteiro (múltiplo de 50) correspondente ao tempo em segundos.

massa = float(input())

times = 0
while massa >= 0.5:
    massa = massa / 2
    times += 1

print(50 * times)