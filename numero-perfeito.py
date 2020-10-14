numeros = int(input())

for i in range(numeros):
    numero = int(input())
    
    divisores = []
    # Pega todos os divisores do numero
    for i in range(numero - 1):
        if numero % (i + 1) == 0:
            divisores.append(i+1)
    
    soma = 0
    for divisor in divisores:
        soma += divisor
    
    if soma == numero:
        print("{} eh perfeito".format(numero))
    else:
        print("{} nao eh perfeito".format(numero))