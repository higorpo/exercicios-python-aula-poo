frase = input()

palavras = frase.replace(' ', '').replace('-', '').replace(',', '')

inverso = ""

for letra in range(len(palavras) - 1, -1, -1):
    inverso += palavras[letra]

if palavras == inverso:
    print("True")
else:
    print("False")
    