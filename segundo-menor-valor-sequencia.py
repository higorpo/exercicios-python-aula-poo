# Dada uma sequência de números inteiros, determine o segundo menor dentre estes valores. Por exemplo, se a sequência de valores for: 10, 15, 7 12, 19 e 3, o segundo menor valor é 7.
# Nos dados de entrada, o primeiro valor indica o tamanho da sequência, ou seja, ele é seguido por esta quantidade de valores, como no exemplo abaixo no que o primeiro valor é 4, indicando que após ele vejam a sequência de quatro valores inteiros.

tamanhoSeq = int(input())

sequencia = []
for i in range(tamanhoSeq):
    sequencia.append(int(input()))
        
print(sorted(sequencia)[1])