while True:
    frases = input()
    
    if frases == "*":
        break

    frases = frases.split(" ")
    
    isTautograma = True
    
    count = 0
    tautograma = ""
    
    for frase in frases:
        if count == 0:
            tautograma = frase[0].lower()
        else:
            if frase[0].lower() != tautograma:
                isTautograma = False
                break
        count += 1
        
    print(isTautograma and "Y" or "N")