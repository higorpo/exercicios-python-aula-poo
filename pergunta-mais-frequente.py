perguntas_freq = []

while True:
    perguntas_realizadas, min_freq = [int(i) for i in input().split()]

    if perguntas_realizadas == 0 and min_freq == 0:
        break

    numeros_perguntas = [int(i) for i in input().split()]
    pergunta_freq = 0

    for i in sorted(set(numeros_perguntas)):
        if numeros_perguntas.count(i) >= min_freq:
            pergunta_freq = i
        
    perguntas_freq.append(pergunta_freq)

for i in perguntas_freq:
    print(i)