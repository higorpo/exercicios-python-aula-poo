# Dada um sequência de números inteiros, determine o maior destes valores. e sua posição na sequência. Nos dados de entrada, o primeiro valor indica o tamanho da sequência, ou seja, ele é seguido por esta quantidade de valores, como no exemplo abaixo no que o primeiro valor é 4, indicando que após ele vejam a sequência de quatro valores inteiros. A saída é composta pelo maior valor e por sua posição na sequência.

tamanhoSeq = int(input())

sequencia = []
for i in range(tamanhoSeq):
    sequencia.append(int(input()))
    
maior = sorted(sequencia)[-1]
print('{} {}'.format(maior, sequencia.index(maior) + 1))