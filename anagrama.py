palavra = input()
anagrama = input()

letrasDaPalavra = list(palavra)

isAnagrama = False

if palavra != anagrama and len(palavra) == len(anagrama):
    # Verifica se todas as palavras estão no anagrama
    for caractere in anagrama:
        if caractere in letrasDaPalavra:
           isAnagrama = True
           del letrasDaPalavra[letrasDaPalavra.index(caractere)]
        else:
            isAnagrama = False
            break
    
print(isAnagrama and len(letrasDaPalavra) == 0)