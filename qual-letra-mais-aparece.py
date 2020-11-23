palavra = input()
splited_palavra = list(palavra)

letras = {}

for letra in splited_palavra:   
    if letra == " ":
        continue

    if letra in letras:
        letras[letra] = letras[letra] + 1
    else:
        letras[letra] = 1

print(letras)
print(max(letras, key=letras.get))