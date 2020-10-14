while True:
    vezesJogadas = int(input())
    
    if vezesJogadas == 0:
        break

    resultadoJogadas = input().split()
          
    johnGanhou = 0
    maryGanhou = 0
    
    for i in resultadoJogadas:
        if int(i) == 0:
            maryGanhou += 1
        else:
            johnGanhou += 1
        
    print("Mary won {} times and John won {} times".format(maryGanhou, johnGanhou))