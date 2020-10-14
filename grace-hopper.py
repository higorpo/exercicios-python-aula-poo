while True:
    palavras = input()
    
    palavras = palavras.split("-")

    isBug = False

    cobol = ['c', 'o', 'b', 'o', 'l']

    for i in range(len(palavras)):
        if cobol[i] not in palavras[i]:
            isBug = True
        
    if isBug:
        print("BUG")
    else:
        print("GRACE HOPPER")
