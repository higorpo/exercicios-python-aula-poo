frases = input().split(" ")

fraseDescriptografada = ""

for frase in frases:
    frase += "  "
    for i in range(1, len(frase), 2):
        fraseDescriptografada += frase[i]

print(fraseDescriptografada)