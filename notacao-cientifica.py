numero = float(input())

notacaoCientifica = '{:e}'.format(numero).split("e")

mantissa = float(notacaoCientifica[0])

mantissaRound = '{:.4f}'.format(round(mantissa, 4))

sinal = "+"

if mantissa < 0:
    sinal = ""

print(sinal + str(mantissaRound) + "E" + notacaoCientifica[1] )